import logging

import pandas as pd
import descriptive_methods
import time
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
import data_exploration_prep as eda

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Flask application
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = 'your_secret_key'  # Secret key for session management
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


# Route for the home page
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard_route'))
    else:
        return render_template('login.html')


# Route for handling login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    logging.debug(f"Login attempt with username: {username}")
    if username == 'test' and password == 'test':
        session['username'] = username
        return redirect(url_for('dashboard_route'))
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard_route():
    eda.prepare_data()
    if 'username' in session:
        # Generate Data Dashboard Charts
        descriptive_methods.save_sex_distribution_chart()  # Sex distribution chart
        descriptive_methods.save_age_distribution_chart()  # Age distribution chart
        descriptive_methods.save_study_time_distribution_chart()  # Study time distribution chart
        descriptive_methods.save_G1_distribution_chart()  # G1 distribution chart
        descriptive_methods.save_G2_distribution_chart()  # G2 distribution chart
        descriptive_methods.save_G3_distribution_chart()  # G3 distribution chart
        descriptive_methods.save_heat_maps()  # Heat maps
        descriptive_methods.save_study_time()  # Study time
        # Render the dashboard template
        return render_template('dashboard_v3.1.html')

    return redirect(url_for('home'))


@app.route('/api/data')
def get_data():
    file_path = '../data/student_data_raw.csv'
    df = eda.load_data(file_path)
    data_head = eda.initial_data_exploration(df)
    data_info = eda.get_dataframe_info(df)
    num_stats = eda.num_stats_analysis(df)
    cat_col_analysis = eda.cat_column_analysis(df)
    oh_data_head = eda.one_hot_encode(df)

    return jsonify({'head': data_head, 'info': data_info, 'num_stats_analysis': num_stats,
                    'cat_col_analysis': cat_col_analysis, 'oh_data_head': oh_data_head})


# Route for logging out
@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('home'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
