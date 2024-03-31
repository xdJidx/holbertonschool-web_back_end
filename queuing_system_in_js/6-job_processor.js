const kue = require('kue');

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Write the queue process
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function with job data
    sendNotification(phoneNumber, message);

    // Mark the job as completed
    done();
});

console.log('Job processor is running...');
