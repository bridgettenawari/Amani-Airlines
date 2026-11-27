# ✈️ Amani Airlines - Web Programming Project

A modern, fully responsive, and interactive airline booking web application. Built from scratch using pure HTML, CSS, and Vanilla JavaScript, with an optional Python/Flask backend for advanced user authentication and database management.

Developed by **Group Mambas**.

## 🚀 Features

### Front-End (HTML/CSS/JS)
- **Modular Architecture:** Organized into Django-style folders (`auth`, `bookings`, `flights`, `css`, `assets`) for scalable code management.
- **Dynamic Homepage:** Responsive UI with a custom dropdown flight search and interactive hover cards.
- **Flight Status Boards:** Arrivals and Departures pages dynamically load data from local JSON files using the JavaScript Fetch API.
- **Hotel Booking:** Beautifully styled hotel cards with login protection.
- **Interactive Search:** Passes user search data via URL parameters to a dynamic results page, simulating a live booking engine.
- **State Management:** Uses `localStorage` to handle user login sessions, checkout flow, and personalized dashboards.

### Back-End (Optional Bonus Feature)
- **Python & Flask:** Handles user authentication (Register/Login) and booking transactions via RESTful API endpoints.
- **SQLite Database:** Automatically creates an `amani_airlines.db` file to store user credentials and confirmed bookings.
- **Graceful Degradation:** If the Python server is not running, the front-end seamlessly falls back to a local "Offline Mode" using `localStorage`, ensuring the website never breaks during a demo.

## 🛠️ Technologies Used
- **Front-end:** HTML5, CSS3 (Flexbox, custom properties, responsive media queries), Vanilla JavaScript (ES6, Fetch API, DOM manipulation).
- **Back-end:** Python 3, Flask, Flask-CORS.
- **Database:** SQLite 3.
- **Icons & Fonts:** Google Fonts (Montserrat), custom SVG icons.

## 📁 Folder Structure
```text
Amani-Airlines-main/
│
├── index.html            # Homepage
├── hotels.html           # Hotels & Accommodation
├── about.html            # About Us
├── account.html          # User Dashboard
├── app.py                # Optional Python Flask Backend
├── README.md             # Project Documentation
│
├── /auth/                # Authentication App
│   ├── login.html
│   └── register.html
│
├── /flights/             # Flight Info App
│   ├── arrivals.html
│   ├── departures.html
│   ├── results.html
│   ├── flights.json
│   └── departures.json
│
├── /bookings/            # Checkout App
│   └── checkout.html
│
├── /css/                 # Stylesheets
│   ├── style.css
│   └── arrivals.css
│
└── /assets/              # Images & Media
    └── /images/

💻 How to Run the Project
Option 1: Front-End Only (No Python Required)

    Clone or download this repository.

    Open the folder in VS Code.

    Double-click index.html to open it in your browser.

    (Note: The site will run in "Offline Mode" using localStorage for login and bookings).
Option 2: Full-Stack Mode (With Python Backend)

To see the database in action:

   1. Ensure Python 3 is installed.

   2. Install the required packages:
       pip install flask flask-cors
   3.Start the Python server from the root directory:
       python3 app.py
   4.Open index.html in your browser. Register a new user, and the data will be saved to amani_airlines.db.

🔍 Viewing the Database (Terminal)

To view the saved data directly from your terminal:
sqlite3 -header -column amani_airlines.db "SELECT * FROM users;"
sqlite3 -header -column amani_airlines.db "SELECT * FROM bookings;"
    