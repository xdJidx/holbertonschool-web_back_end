export default class HolbertonCourse {
  // Constructor to initialize the attributes.
  constructor(name, length, students) {
    // Initialize and validate the 'name' attribute.
    this._name = this.validateString(name, 'Name');

    // Initialize and validate the 'length' attribute.
    this._length = this.validateNumber(length, 'Length');

    // Initialize and validate the 'students' attribute.
    this._students = this.validateArray(students, 'Students');
  }

  // Getter and setter for the 'name' attribute.
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this.validateString(newName, 'Name');
  }

  // Getter and setter for the 'length' attribute.
  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = this.validateNumber(newLength, 'Length');
  }

  // Getter and setter for the 'students' attribute.
  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = this.validateArray(newStudents, 'Students');
  }

  // Helper method to validate string attributes.
  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attributeName} must be a string`);
    }
    return value;
  }

  // Helper method to validate number attributes.
  validateNumber(value, attributeName) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new TypeError(`${attributeName} must be a number`);
    }
    return value;
  }

  // Helper method to validate array attributes.
  validateArray(value, attributeName) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${attributeName} must be an array`);
    }
    return value;
  }
}