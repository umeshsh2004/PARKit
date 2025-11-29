from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment/', views.payment_page, name='payment_page'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('process-payment/', views.process_payment, name='process_payment'),
]
