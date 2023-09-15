export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter for the 'name' attribute.
  get name() {
    return this._name;
  }

  // Getter for the 'code' attribute.
  get code() {
    return this._code;
  }

  // Custom toString method to return the airport code.
  toString() {
    return `[${this._code}]`;
  }
}
