// const { ipcRenderer } = require('electron');

// Function to generate the table based on the API response
function generateTable(data) {
    // Generate the table HTML dynamically based on the data

    // Add sorting, searching, and pagination logic

    // Display the table in the "tableContainer" div
}

(function validateMessages() {
    var schoolUrl = document.getElementById("schoolUrl");

    schoolUrl.addEventListener("invalid", function (event) {
        event.target.setCustomValidity("Please enter a valid KVS URL.");
    });

    schoolUrl.addEventListener("input", function (event) {
        event.target.setCustomValidity("");
    });
    
    var startingTC = document.getElementById("startingTC");

    startingTC.addEventListener("invalid", function (event) {
        event.target.setCustomValidity("Please enter a valid TC Number.");
    });

    startingTC.addEventListener("input", function (event) {
        event.target.setCustomValidity("");
    });
})();

// Handle form submission
document.getElementById('dataForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Getting form data
    const schoolUrl = document.getElementById('schoolUrl').value;
    const startingTC = document.getElementById('startingTC').value;
    const range = document.getElementById('range').value;
    const logData = document.getElementById('logData').checked;

    const formData = { schoolUrl, startingTC, range, logData };
    console.log(formData, "formData");

    // Validate form input
    if (!schoolUrl || !startingTC || !range) {
        alert('Please fill out all fields');
        return;
    }

    // const tcData = require('./index');
    console.log(tcData(schoolUrl, startingTC, range, logData), "tcData");


    // // Sending data to main process
    // ipcRenderer.send('form-data', formData);

    // // Handle response from main process
    // ipcRenderer.on('form-data-response', (event, response) => {
    //     if (response) {
    //         console.log(response);
    //         // generateTable(response);
    //     }
    // });
});