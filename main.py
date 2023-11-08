 
# Import the necessary modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Define the database connection
conn = sqlite3.connect('registrants.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS registrants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT
                )''')

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        # Insert the data into the database
        c.execute("INSERT INTO registrants (first_name, last_name, email) VALUES (?, ?, ?)",
                  (first_name, last_name, email))
        conn.commit()

        # Send an email to confirm attendance
        # ...

        # Redirect to the home page
        return redirect(url_for('home'))

    return render_template('register.html')

# Define the main function
if __name__ == '__main__':
    app.run(debug=True)


main.py file:


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('registrants.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS registrants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT
            )''')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        c.execute("INSERT INTO registrants (first_name, last_name, email) VALUES (?, ?, ?)",
                  (first_name, last_name, email))
        conn.commit()

        # Send an email to confirm attendance
        # ...

        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
