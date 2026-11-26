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
    
    # NEW: Bookings Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            item_name TEXT NOT NULL,
            item_price TEXT NOT NULL,
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

# NEW: Booking Route
@app.route('/api/book', methods=['POST'])
def book():
    data = request.get_json()
    email = data.get('email')
    item_name = data.get('item_name')
    item_price = data.get('item_price')

    conn = sqlite3.connect('amani_airlines.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (user_email, item_name, item_price) VALUES (?, ?, ?)", (email, item_name, item_price))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Booking saved to database!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)