const express = require('express');
const app = express();
const PORT = 7865;

// Endpoint GET /available_payments
app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

// Endpoint POST /login
app.post('/login', (req, res) => {
    const { userName } = req.body;
    res.send(`Welcome ${userName}`);
});

app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

module.exports = app; // Export the app for testing
