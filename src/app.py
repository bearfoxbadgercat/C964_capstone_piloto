from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = 'your_secret_key'  # Needed for session management


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'test' and password == 'test':
        print("You're using def login() in app.py")
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('main.html')
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
