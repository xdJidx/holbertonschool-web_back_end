const request = require('supertest');
const app = require('./api');

describe('Test /login endpoint', () => {
    it('POST /login - Responds with Welcome message', async () => {
        const response = await request(app)
            .post('/login')
            .send({ userName: 'Betty' })
            .expect('Content-Type', /json/)
            .expect(200);

        expect(response.text).toBe('Welcome Betty');
    });
});

describe('Test /available_payments endpoint', () => {
    it('GET /available_payments - Responds with correct payment_methods object', async () => {
        const response = await request(app)
            .get('/available_payments')
            .expect('Content-Type', /json/)
            .expect(200);

        expect(response.body).toEqual({
            payment_methods: {
                credit_cards: true,
                paypal: false
            }
        });
    });
});
