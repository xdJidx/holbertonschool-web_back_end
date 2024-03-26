// 3-payment.test.js

const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  afterEach(() => {
    sinon.restore();
  });

  it('should call Utils.calculateNumber with the correct arguments and log the result', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    chai.expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    chai.expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });
});
