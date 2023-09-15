// Create a unique symbol for cloning
const cloneSymbol = Symbol("clone");

class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for the 'brand' attribute.
  get brand() {
    return this._brand;
  }

  // Getter for the 'motor' attribute.
  get motor() {
    return this._motor;
  }

  // Getter for the 'color' attribute.
  get color() {
    return this._color;
  }

  // Method to clone the car.
  cloneCar() {
    const clonedCar = new this.constructor(); // Create a new instance of the same class

    // Copy properties to the cloned object
    for (const key of Object.getOwnPropertyNames(this)) {
      if (key !== cloneSymbol) {
        clonedCar[key] = this[key];
      }
    }

    return clonedCar;
  }
}

export default Car;
