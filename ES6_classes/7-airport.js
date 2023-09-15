export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a String');
    }
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a String');
    }

    this._name = name;
    this._code = code;
  }

  // Getter for the 'name' attribute.
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  // Getter for the 'code' attribute.
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value;
  }

  // Custom toString method to return the airport code.
  toString() {
    return `[object ${this._code}]`;
  }
}
