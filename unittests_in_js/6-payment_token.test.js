// 6-payment_token.test.js

const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', function () {
    it('should return a successful response when success is true', function (done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                assert.deepStrictEqual(response, { data: 'Successful response from the API' });
                done();
            })
            .catch(error => done(error));
    });

    it('should throw an error when success is false', function (done) {
        getPaymentTokenFromAPI(false)
            .then(() => {
                done(new Error('The promise should have been rejected'));
            })
            .catch(error => {
                assert.strictEqual(error.message, 'API call failed');
                done();
            });
    });
});
