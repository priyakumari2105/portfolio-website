from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Connect to database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    ''')

    # Insert data
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    # ✅ SHOW BOTH SUCCESS + DATA
    return render_template(
        'contact.html',
        name=name,
        email=email,
        message=message,
        success=True
    )

# Run app
if __name__ == "__main__":
    app.run(debug=True)