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

// Next thing I'm going to do is look at the one hot encoding table

