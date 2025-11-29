# ParkIT - Parking Slot Reservation System 🚗

ParkIT is a web-based application that simplifies the process of reserving parking slots. It offers user-friendly dashboards for both users and administrators to manage reservations, payments, and parking slots efficiently.

---

## Features 📋

### Authentication (Login)
- Admin Login to access Admin Dashboard
- User Login to access User Dashboard

### User Dashboard
- **Reserve Slots**: Users can view available parking slots and reserve them by specifying start and end times.
- **Payment Gateway**: Integrated payment system with dynamic pricing:
  - First 2 hours: Free
  - Next 2 hours: ₹150
  - Every subsequent 2 hours: +₹100
  - Full day (10+ hours): ₹500/day
- **Transaction History**: View all previous transactions with details of amount paid and parking duration.
- **Submit Feedback**: Users can share their experience or provide suggestions directly through the dashboard.

### Admin Dashboard
- **Manage Slots**: Admins can create, delete, and assign parking slots to specific locations.
- **Reservation Overview**: View all current and past reservations, along with user details.
- **Payments Overview**: Access a detailed report of payments, including amount paid, duration parked, and user details.

---

## Tech Stack 💻

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django
- **Database**: SQLite (default Django database)
- **Payment Integration**: Simulated payment gateway for testing purposes
- **CSS Framework**: Font Awesome for icons

---

## Project Structure 🗂️
```
plaintext
ParkIT/
├── parkit/  # Django project settings and configurations
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── reservations/          # App for managing slots, reservations, and payments
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/             # HTML templates
│   ├── master.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   └── ...
├── db.sqlite3             # Database file
├── manage.py              # Django management script
└── README.md              # Project documentation

```
---

## Installation and Setup 🚀

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Siddhubn/PARKit.git
   cd parkit
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Mac\Linux: source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser #enter login credentials through the terminal for the initial admin login - username, email, password.
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. Access the app at `http://127.0.0.1:8000/`.

---

## Usage 📖

1. **Register as a User or Admin**:
   - Users can register and reserve parking slots.
   - Admins can log in to manage parking slots and reservations.

2. **Reserve Slots**:
   - Navigate to the user dashboard, choose an available slot, and reserve it by specifying the timing.

3. **Payments**:
   - Pay the calculated amount and confirm your reservation.

4. **Admin Features**:
   - Add or remove slots and view all reservations and payment details.

---

## Future Enhancements 🌟

- **Real-Time Notifications**: Notify users about available slots.
- **Google Maps Integration**: Add real-time parking location mapping.
- **Dynamic Pricing**: Flexible pricing based on demand and time of day.
- **Mobile App**: Develop a mobile app for a seamless user experience.

---

## Snapshots 📷
- Click on [This](./Parkit Snapshots) to view the Snapshots of the UI of the WebApp.

---

## Contributing 🤝

Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Added feature-name"`.
4. Push the changes: `git push origin feature-name`.
5. Create a Pull Request.

---

## License 📜

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements 🙏

- **Font Awesome** for the beautiful icons.
- **Django** for making web development easy and scalable.

---

### Demo 🎥

- URL: [PARKit](https://parkit-4od3.onrender.com/)
---
