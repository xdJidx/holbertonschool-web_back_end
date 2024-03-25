const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    describe('when type is SUM', function () {
      it('should return the rounded sum of a and b', function () {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      });
    });
  
    describe('when type is SUBTRACT', function () {
      it('should return the rounded difference of a and b', function () {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      });
    });
  
    describe('when type is DIVIDE', function () {
      it('should return the rounded quotient of a and b', function () {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      });
  
      it('should return Error when b is 0', function () {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      });
    });
  });
