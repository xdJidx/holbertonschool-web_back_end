export default function cleanSet(set, startString) {
  const string = [];

  if (
    typeof set !== 'object'
        || typeof startString !== 'string'
        || startString.length === 0) {
    return '';
  }

  for (const value of set) {
    // Check if the current value starts with startString
    if (value && value.startsWith(startString)) {
      // If yes, add the rest of the string (excluding startString) to the matchingValues array
      string.push(value.slice(startString.length));
    }
  }

  return string.join('-');
}
