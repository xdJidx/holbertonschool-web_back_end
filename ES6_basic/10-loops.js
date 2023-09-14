export default function appendToEachArrayValue(array, appendString) {
  // declare table
  const newArray = [];

  // loops 
  for (const value of array) {
    // add value in table
    newArray.push(appendString + value);
  }
  return newArray;
}