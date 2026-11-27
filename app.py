from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) 

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    
    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Bookings Table (UPDATED WITH BOOKING_TYPE)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            item_name TEXT NOT NULL,
            item_price TEXT NOT NULL,
            booking_type TEXT DEFAULT 'Hotel',
            booking_date DATE DEFAULT CURRENT_DATE
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# --- API ROUTES ---
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        return jsonify({"status": "success", "message": "Account created in database!"})
    except sqlite3.IntegrityError:
        return jsonify({"status": "error", "message": "Email already exists!"}), 400
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "success", "message": "Login successful!"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route('/api/book', methods=['POST'])
def book():
    data = request.get_json()
    email = data.get('email')
    item_name = data.get('item_name')
    item_price = data.get('item_price')
    booking_type = data.get('booking_type', 'Hotel') # NEW

    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (user_email, item_name, item_price, booking_type) VALUES (?, ?, ?, ?)", (email, item_name, item_price, booking_type))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Booking saved to database!"})

# Fetch bookings for the Account Dashboard
@app.route('/api/my-bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    
    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    cursor.execute("SELECT item_name, item_price, booking_type, booking_date FROM bookings WHERE user_email = ?", (email,))
    bookings = cursor.fetchall()
    conn.close()

    result = []
    for b in bookings:
        result.append({
            "item_name": b[0],
            "item_price": b[1],
            "booking_type": b[2],
            "booking_date": b[3]
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)