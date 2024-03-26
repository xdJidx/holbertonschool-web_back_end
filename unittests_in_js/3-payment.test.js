// 3-payment.test.js

const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', function () {
    it('should call Utils.calculateNumber with correct arguments', function () {
        const spy = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        sinon.assert.calledOnce(spy);
        sinon.assert.calledWithExactly(spy, 'SUM', totalAmount, totalShipping);

        spy.restore(); // Restore the original method after the test
    });
});
