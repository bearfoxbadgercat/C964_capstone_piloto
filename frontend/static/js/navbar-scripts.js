function showFeature(featureId) {
    // Hide all sections
    const features = document.querySelectorAll('.feature');
    features.forEach(feature => {
        feature.style.display = 'none';
    });

    // Show the selected section
    const selectedFeature = document.getElementById(featureId);
    if (selectedFeature) {
        selectedFeature.style.display = 'flex';
    }
}

// Show the first feature by default
window.onload = () => {
    showFeature('data-pilot-f');
};

// Add keyboard support for div buttons
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
            button.click();
        }
    });
});

function updateValue(val) {
    document.getElementById("sliderValue").textContent = val;
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/data')
        .then(response => response.json()) // Parse the JSON response


        .then(data => {
            let tableHead = document.querySelector('#table-head');
            let tableBody = document.querySelector('#table-body');
            let dataInfo = document.querySelector('#data-info');
            let numStatsAnalysis = document.querySelector('#num-stats-analysis');
            let catAnalysis = document.querySelector('#cat-analysis');
            let ohTableHead = document.querySelector('#oh-table-head');
            let ohTableBody = document.querySelector('#oh-table-body');

            // Define the desired column order
            let columnOrder = [
                "id", "school", "sex", "age", "address", "famsize", "Pstatus",
                "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian",
                "traveltime", "studytime", "failures", "schoolsup", "famsup",
                "paid", "activities", "nursery", "higher", "internet", "romantic",
                "famrel", "freetime", "goout", "Dalc", "Walc", "health",
                "absences", "G1", "G2", "G3"
            ];

            let ohColumnOrder = [
                'age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences',
                'school_GP', 'school_MS', 'sex_F', 'sex_M',
                'address_R', 'address_U', 'famsize_GT3', 'famsize_LE3', 'Pstatus_A',
                'Pstatus_T', 'Mjob_at_home', 'Mjob_health', 'Mjob_other',
                'Mjob_services', 'Mjob_teacher', 'Fjob_at_home', 'Fjob_health',
                'Fjob_other', 'Fjob_services', 'Fjob_teacher', 'reason_course',
                'reason_home', 'reason_other', 'reason_reputation', 'guardian_father',
                'guardian_mother', 'guardian_other', 'schoolsup_no', 'schoolsup_yes',
                'famsup_no', 'famsup_yes', 'paid_no', 'paid_yes', 'activities_no',
                'activities_yes', 'nursery_no', 'nursery_yes', 'higher_no',
                'higher_yes', 'internet_no', 'internet_yes', 'romantic_no',
                'romantic_yes','average_grade'
            ];

            // Populate table headers in the defined order
            columnOrder.forEach(key => {
                let th = document.createElement('th');
                th.textContent = key;
                tableHead.appendChild(th);
            });

            // Populate one hot encoded table headers in the defined order
            ohColumnOrder.forEach(key => {
                let th = document.createElement('th');
                th.textContent = key;
                ohTableHead.appendChild(th);
            });

            // Populate table rows in the defined order
            data.head.forEach(row => {
                let tr = document.createElement('tr');
                columnOrder.forEach(key => {
                    let td = document.createElement('td');
                    td.textContent = row[key];
                    tr.appendChild(td);
                });
                tableBody.appendChild(tr);
            });

            // Populate DataFrame info
            dataInfo.textContent = data.info;

            // Populate the num stats
            numStatsAnalysis.textContent = data.num_stats_analysis;


             // Populate categorical column analysis
            catAnalysis.textContent = data.cat_col_analysis;


            // Populate one hot encoded table rows in the defined order
            data.oh_data_head.forEach(row => {
                let tr = document.createElement('tr');
                ohColumnOrder.forEach(key => {
                    let td = document.createElement('td');
                    td.textContent = row[key];
                    tr.appendChild(td);
                });
                ohTableBody.appendChild(tr);
            });
        })

        .catch(error => console.error('Error fetching data:', error));
});

function selectOption(option) {
    document.getElementById('dropdownButton').innerText = option;
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/get-model-names')
        .then(response => response.json())
        .then(data => {
            const dropdownContent = document.getElementById('dropdownContent');
            dropdownContent.innerHTML = '';  // Clear any existing options
            data.forEach(file => {
                const link = document.createElement('a');
                link.href = '#';
                link.textContent = file;
                link.onclick = () => {
                    document.getElementById('dropdownButton').innerText = file;
                };
                dropdownContent.appendChild(link);
            });
        })
        .catch(error => console.error('Error fetching dataset names:', error));
});

//  Updates the value of the slider
function updateValue(value) {
  document.getElementById('sliderValue').textContent = value;
}


function buildModel() {
  var sliderValue = document.getElementById('mySlider').value;

  fetch('/build_model', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'sliderValue=' + sliderValue
  })
  .then(response => response.json())
  .then(data => {
    // Update the MAE score in the HTML
    document.getElementById('maeScore').innerText = "MAE: " + data.result;
  })
  .catch(error => console.error('Error:', error));
}

function getStudent() {
    var studentId = document.getElementById('studentIdInput').value;
    // Check if the input is numeric and within the specified range
    if (!/^\d+$/.test(studentId) || studentId < 0 || studentId > 390) {
        alert("Please enter a valid numeric ID between 0 and 390.");
    } else {
        document.getElementById('studentIdDisplay').value = studentId;
    }
}

function updateStudyTimeValue(value) {
    document.getElementById('studyTimeValue').textContent = value;
}

function fetchStudentData(index) {
    fetch('/api/get_student/' + index)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            alert(data.error);
            return; // Stop further execution in case of an error
        }

        // Update study time slider
        if (data.study_time) {
            var studyTime = parseInt(data.study_time, 10);
            document.getElementById('studyTimeSlider').value = studyTime;
            document.getElementById('studyTimeValue').textContent = studyTime;
        }

        // Update internet access radio buttons
        if (data.internet) {
            if (data.internet === 'yes') {
                document.getElementById('internet_yes').checked = true;
            } else if (data.internet === 'no') {
                document.getElementById('internet_no').checked = true;
            }
        }

        // Update the activities radio buttons
        if (data.activities) {
            if (data.activities === 'yes') {
                document.getElementById('activities_yes').checked = true;
            } else if (data.activities === 'no') {
                document.getElementById('activities_no').checked = true;
            }
        }


        // Update the paid radio buttons
        if(data.paid){
            if(data.paid === 'yes'){
                document.getElementById('paid_yes').checked = true;
            } else if(data.paid === 'no'){
                document.getElementById('paid_no').checked = true;
            }
        }

    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to fetch data');
    });
}

function updateInternetAccess(internetValue) {
    console.log("Received internet access value: ", internetValue); // This will show the value in the browser's console
    if (internetValue === 'yes') {
        document.getElementById('internet_yes').checked = true;
    } else if (internetValue === 'no') {
        document.getElementById('internet_no').checked = true;
    }
}


function getStudent() {
    var studentId = document.getElementById('studentIdInput').value;
    if (!/^\d+$/.test(studentId) || studentId < 0 || studentId > 390) {
        alert("Please enter a valid numeric ID between 0 and 390.");
    } else {
        document.getElementById('studentIdDisplay').value = studentId;
        fetchStudentData(studentId);
    }
}

function predict() {
    var modelName = document.getElementById('dropdownButton').innerText;  // Capture the model name from the dropdown
    var studentId = document.getElementById('studentIdDisplay').value;    // Capture the Student ID from the display input field
    var studyTime = document.getElementById('studyTimeSlider').value;     // Capture the Study Time from the slider
    var internetAccess = document.querySelector('input[name="internet"]:checked').value; // Determine which Internet Access radio button is checked
    var activities = document.querySelector('input[name="activities"]:checked').value;    // Determine which Activities radio button is checked
    var paidClasses = document.querySelector('input[name="paid"]:checked').value;         // Determine which Paid Classes radio button is checked

    // Check if the Student ID or model name is empty
    if (!studentId) {
        alert("Please select a student first.");
        return; // Stop the execution of the rest of the function
    }

    if (modelName === 'Select Model') {
        alert("Please select a model first.");
        return; // Stop the execution if no model is selected
    }

    // Create the data object to send to the server
    var postData = {
        studentId: studentId,
        studyTime: studyTime,
        internetAccess: internetAccess,
        activities: activities,
        paidClasses: paidClasses,
        modelName: modelName
    };

    // Make the fetch request to the server
    fetch('/predict_grade', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Setting the content type header to application/json
        },
        body: JSON.stringify(postData)  // Convert the JavaScript object into a JSON string
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("Error: " + data.error);
        } else {
            alert("Predicted Score: " + data.prediction);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to fetch data');
    });
}



// Attach this function to the Predict button
document.getElementById('predictButton').addEventListener('click', gatherFormData);



