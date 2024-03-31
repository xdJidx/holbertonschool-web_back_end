const kue = require('kue');

const queue = kue.createQueue();
const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach((job) => {
        const singleJob = queue.create('push_notification_code_3', job).save(
            (err) => {
                if (!err) console.log(`Notification job created: ${singleJob.id}`);
            });

        singleJob.on('complete', () => console.log(`Notification job ${singleJob.id} completed`));
        singleJob.on('failed', (err) => console.log(`Notification job ${singleJob.id} failed: ${err}`));
        singleJob.on('progress', (progress) => console.log(`Notification job ${singleJob.id} ${progress}% complete`));
    });
}

module.exports = createPushNotificationsJobs;
