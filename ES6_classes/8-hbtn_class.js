export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Getter for the 'size' attribute.
  get size() {
    return this._size;
  }

  // Getter for the 'location' attribute.
  get location() {
    return this._location;
  }

  // Define a custom casting behavior to Number.
  valueOf() {
    return this._size;
  }

  // Define a custom casting behavior to String.
  toString() {
    return this._location;
  }
}
