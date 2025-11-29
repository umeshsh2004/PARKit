from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.decorators import user_passes_test
from .models import User,ParkingSlot, Reservation,Transaction

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    return render(request, 'contactus.html')

def about_us(request):
    return render(request, 'about_us.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).first():
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, 'Username already exists!')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if request.method == 'POST':
        if 'reserve_slot' in request.POST:
            slot_id = request.POST.get('slot_id')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')

            try:
                slot = ParkingSlot.objects.get(id=slot_id, is_reserved=False)
                if start_time and end_time:
                    reservation = Reservation.objects.create(
                        user=request.user,
                        slot=slot,
                        start_time=start_time,
                        end_time=end_time
                    )
                    slot.is_reserved = True
                    slot.reserved_start_time = start_time
                    slot.reserved_end_time = end_time
                    slot.save()

                    Transaction.objects.create(
                        user=request.user,
                        reservation=reservation,
                        amount=100.00  
                    )

                    return redirect('payment_page') 
                else:
                    messages.error(request, 'Invalid time details!')
            except ParkingSlot.DoesNotExist:
                messages.error(request, 'Slot is already reserved or does not exist!')
        elif 'submit_feedback' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            feedback = request.POST.get('feedback')
            reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
            reservation.feedback = feedback
            reservation.save()
            messages.success(request, 'Feedback submitted successfully!')

    slots = ParkingSlot.objects.exclude(is_reserved=True)
    user_reservations = Reservation.objects.filter(user=request.user)
    user_transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'slots': slots,
        'reservations': user_reservations,
        'transactions': user_transactions
    })

@login_required
def payment_page(request):
    return render(request, 'payments.html')

def admin_check(user):
    return user.is_staff

@user_passes_test(admin_check)
def admin_dashboard(request):
    if request.method == 'POST':
        if 'create_slot' in request.POST:
            slot_number = request.POST.get('slot_number')
            location = request.POST.get('location')
            if slot_number and location:
                ParkingSlot.objects.create(slot_number=slot_number, location=location)
                messages.success(request, 'Slot created successfully!')
            else:
                messages.error(request, 'Invalid slot details!')
        elif 'delete_slot' in request.POST:
            slot_id = request.POST.get('slot_id')
            try:
                slot = ParkingSlot.objects.get(id=slot_id)
                slot.delete()
                messages.success(request, 'Slot deleted successfully!')
            except ParkingSlot.DoesNotExist:
                messages.error(request, 'Slot not found!')

    slots = ParkingSlot.objects.all()
    reservations = Reservation.objects.select_related('user', 'slot').all()
    transactions = Transaction.objects.select_related('reservation').all()

    for transaction in transactions:
        reservation_duration = transaction.reservation.end_time - transaction.reservation.start_time
        transaction.duration_in_hours = reservation_duration.total_seconds() / 3600

    return render(request, 'admin_dashboard.html', {
        'slots': slots,
        'reservations': reservations,
        'transactions': transactions
    })

@login_required
def process_payment(request):
    if request.method == "POST":
        reservation_id = request.POST.get("reservation_id")
        reservation = get_object_or_404(Reservation, id=reservation_id)
        amount = reservation.calculate_price()

        reservation.slot.is_reserved = True
        reservation.slot.save()

        Transaction.objects.create(reservation=reservation, amount_paid=amount)
        return redirect("user_dashboard")
    return redirect("payments")