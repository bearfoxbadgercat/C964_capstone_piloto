import logging
import os

import pandas as pd
import descriptive_methods
import time
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
import data_exploration_prep as eda
import ML_method_algorithms as ml

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


@app.route('/get-model-names')
def get_dataset_names():
    # Assuming 'data' is one level up from the directory containing app.py
    folder = os.path.join(os.path.dirname(__file__), '../models')
    datasets = [f for f in os.listdir(folder) if f.endswith('joblib')]
    return jsonify(datasets)


@app.route('/build_model', methods=['POST'])
def build_model():
    num_leafs = request.form['sliderValue']
    mae = ml.create_rf_model(num_leafs)
    return jsonify(result=f"Model built with MAE: {mae}")


@app.route('/api/get_student/<int:index>', methods=['GET'])
def get_student(index):
    file_path = '../data/student_data_raw.csv'
    try:
        df = pd.read_csv(file_path)
        study_time = df.iloc[index]['studytime']
        internet = df.iloc[index]['internet']
        activities = df.iloc[index]['activities']
        paid = df.iloc[index]['paid']
        # Get the average grade for the student at the given index from g1, g2, and g3
        average_grade = (df.iloc[index]['G1'] + df.iloc[index]['G2'] + df.iloc[index]['G3']) / 3

        # Round the average_grade
        average_grade = round(average_grade, 2)

        # Need to make study_time a string to jsonify it
        study_time = str(study_time)
        internet = str(internet)
        activities = str(activities)
        paid = str(paid)

        print(f"Study time: {study_time}, Internet: {internet}, Activities: {activities}, Paid: {paid}")
        # Jsonify the response
        return jsonify({'study_time': study_time, 'internet': internet, 'activities': activities,
                        'paid': paid, 'average_grade': average_grade})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/predict_grade', methods=['POST'])
def predict_grade():
    data = request.get_json()  # This assumes you send data as JSON from your frontend
    print(data)

    try:
        # Extracting data from the POST request
        row_number = int(data['studentId'])
        study_time = int(data['studyTime'])
        internet = data['internetAccess']
        activities = data['activities']
        paid = data['paidClasses']
        model_name = data['modelName']  # Ensure this is included in the request from the frontend

        # Predict the grade using the predict_score function
        prediction = ml.predict_score(row_number, study_time, internet, activities, paid, model_name)

        rounded_prediction = round(prediction[0], 2)  # Assuming prediction is an array with at least one element

        # Return the prediction result
        return jsonify({'prediction': rounded_prediction})
    except Exception as e:
        print("Error:", e)  # It's also helpful to print out errors to the console
        return jsonify({'error': str(e)}), 400


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
