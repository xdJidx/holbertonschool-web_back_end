// utils.js

const Utils = {
  calculateNumber(type, a, b) {
    const num1 = Math.round(a);
    const num2 = Math.round(b);

    if (type === 'SUM') {
      return num1 + num2;
    } else if (type === 'SUBTRACT') {
      return num1 - num2;
    } else if (type === 'DIVIDE') {
      if (num2 === 0) throw new Error('Cannot divide by 0');
      return num1 / num2;
    } else {
      throw new Error('Invalid calculation type. Valid types are: SUM, SUBTRACT, DIVIDE');
    }
  }
};
