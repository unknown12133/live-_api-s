const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
// Basic Health Check
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the API', status: 'OK', timestamp: new Date() });
});

app.get('/api/health', (req, res) => {
    res.json({ status: 'UP', uptime: process.uptime() });
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
