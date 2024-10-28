// server.js
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

let healthData = {
    heartRate: 0,
    pulse: 0,
    temperature: 0,
    bloodPressure: { systolic: 0, diastolic: 0 },
    bloodSugar: 0,
};

// Function to generate random health data
function generateRandomHealthData() {
    healthData.heartRate = Math.floor(Math.random() * (120 - 60 + 1)) + 60;  // Random heart rate between 60 and 120
    healthData.pulse = Math.floor(Math.random() * (100 - 50 + 1)) + 50;  // Random pulse between 50 and 100
    healthData.temperature = (Math.random() * (102 - 97) + 97).toFixed(1);  // Random temperature between 97°F and 102°F
    healthData.bloodPressure.systolic = Math.floor(Math.random() * (140 - 90 + 1)) + 90;  // Random systolic BP
    healthData.bloodPressure.diastolic = Math.floor(Math.random() * (90 - 60 + 1)) + 60;  // Random diastolic BP
    healthData.bloodSugar = Math.floor(Math.random() * (200 - 70 + 1)) + 70;  // Random blood sugar between 70 and 200
}

// Set an interval to update the health data every second
setInterval(generateRandomHealthData, 1000);

// Endpoint to get the latest health data
app.get('/health', (req, res) => {
    res.json(healthData);
});

const PORT = 3000;  // Change this port number if necessary
app.listen(PORT, () => {
    console.log(`Health data server running on http://localhost:${PORT}`);
});
