// 4-payment.test.js

const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function () {
    afterEach(function () {
        sinon.restore();
    });

    it('should call Utils.calculateNumber with correct arguments and log the correct message', function () {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const consoleSpy = sinon.spy(console, 'log');
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        sinon.assert.calledOnceWithExactly(stub, 'SUM', totalAmount, totalShipping);
        sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 10');

        stub.restore(); // Restore the original method after the test
        consoleSpy.restore(); // Restore the original console.log method
    });
});
