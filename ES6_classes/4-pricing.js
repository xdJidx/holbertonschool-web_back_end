import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
        throw new TypeError('Amount must be a Number');
        }

    if (!(currency instanceof Currency)) {
        throw new TypeError('currency must be a currency');
        }

    this._amount = amount;
    this._currency = currency;
  }

  // Getter for the 'amount' attribute.
  get amount() {
    return this._amount;
  }

  // Setter for the 'amount' attribute.
  set amount(newAmount) {
    this._amount = newAmount;
  }

  // Getter for the 'currency' attribute.
  get currency() {
    return this._currency;
  }

  // Setter for the 'currency' attribute.
  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  // Method to display the full price information.
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert the price using a conversion rate.
  static convertPrice(amount, convertRate) {
    return amount * convertRate;
  }
}
