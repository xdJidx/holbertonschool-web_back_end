import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Create a queue with Kue
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
    before(() => {
        // Enter test mode without processing jobs
        queue.testMode.enter();
    });

    after(() => {
        // Clear the queue and exit test mode after tests
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('displays an error message if jobs is not an array', () => {
        // Call createPushNotificationsJobs with a non-array argument
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    });

    it('creates two new jobs to the queue', () => {
        // Define a sample jobs array
        const jobs = [
            { phoneNumber: '1234567890', message: 'Hello World' },
            { phoneNumber: '0987654321', message: 'Bonjour le monde' }
        ];

        // Spy on the save method of the job object
        const saveSpy = sinon.spy();

        // Stub the job object with the spy
        sinon.stub(queue, 'create').callsFake(() => ({
            save: saveSpy
        }));

        // Call createPushNotificationsJobs with the sample jobs array
        createPushNotificationsJobs(jobs, queue);

        // Validate that the save method is called twice
        expect(saveSpy.calledTwice).to.be.true;
    });
});
