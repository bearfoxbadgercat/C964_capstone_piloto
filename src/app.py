from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
import pandas as pd

# Initialize the Flask application
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = 'your_secret_key'  # Secret key for session management


# Route for the home page
@app.route('/')
def home():
    # Redirect to dashboard if user is logged in
    if 'username' in session:
        return redirect(url_for('dashboard'))
    # Otherwise, render the login page
    return render_template('login.html')


# Route for handling login
@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the form
    username = request.form['username']
    password = request.form['password']
    # Simple authentication logic
    if username == 'test' and password == 'test':
        # Store username in session and redirect to dashboard
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        # Flash message for invalid credentials and redirect to home
        flash('Invalid username or password!')
        return redirect(url_for('home'))


# Route for the dashboard
@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'username' in session:
        # Render the main dashboard page
        return render_template('main.html')
    # Redirect to home if not logged in
    return redirect(url_for('home'))


# Route for logging out
@app.route('/logout')
def logout():
    # Remove username from session
    session.pop('username', None)
    # Redirect to home
    return redirect(url_for('home'))


# Route for the Copilot page
@app.route('/copilot')
def copilot():
    # Check if user is logged in
    if 'username' in session:
        # Render the Copilot page
        return render_template('copilot.html')
    # Redirect to home if not logged in
    return redirect(url_for('home'))


# Route for the Pathfinder page
@app.route('/pathfinder')
def pathfinder():
    # Check if user is logged in
    if 'username' in session:
        # Render the Pathfinder page
        return render_template('pathfinder.html')
    # Redirect to home if not logged in
    return redirect(url_for('home'))


# Route for the Autopilot page
@app.route('/autopilot')
def autopilot():
    # Check if user is logged in
    if 'username' in session:
        return render_template('autopilot.html')
    # Redirect to home if not logged in
    return redirect(url_for('home'))


# Route to load data
@app.route('/load_data', methods=['GET'])
def load_data():
    try:
        # Path to the CSV file
        file_path = os.path.abspath(os.path.join(app.root_path, '..', 'data', 'student_data_raw.csv'))
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)
        # Convert the DataFrame to a JSON string for easier handling in JavaScript
        data = df.head().to_json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
