from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = 'your_secret_key'  # Needed for session management


# Add a new route for the home
@app.route('/')
def home():
    print("Session keys:", session.keys())  # Print session keys for debugging
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


# Add a new route for the login
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate the user and redirect to the dashboard or back to home on failure.
    """
    username = request.form['username']
    password = request.form['password']
    if username == 'test' and password == 'test':
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))  # Correctly redirect to home on failure


# Add a new route for the dashboard
@app.route('/dashboard')
def dashboard():
    """
    Render the dashboard page if the user is logged in, otherwise redirect to home.
    """
    if 'username' in session:
        return render_template('main.html')
    return redirect(url_for('home'))


# Add a new route for the logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
