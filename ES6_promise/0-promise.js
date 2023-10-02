// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Simulate an API call or any asynchronous operation
    setTimeout(() => {
      // Resolve the Promise with some data
      resolve('API response data');
      // You can also reject the Promise in case of an error
      // reject('API request failed');
    }, 1000); // Simulating a delay of 1 second
  });
}
