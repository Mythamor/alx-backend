const createPushNotificationsJobs = require('./8-job.js'); 
const Queue = require('kue'); // Import Kue for queue management
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');

// Enable chai as promised
chai.use(chaiAsPromised);
const expect = chai.expect;

// Create a test suite
describe('createPushNotificationsJobs', function () {
    let queue;

    // Before each test, create a new queue
    beforeEach(function () {
        queue = Queue.createQueue();
    });

    // After each test, clear the queue and exit the test mode
    afterEach(function (done) {
        queue.testMode.clear(done);
    });

    // Test case for createPushNotificationsJobs function
    it('should add jobs to the queue', function () {
        // Enter test mode without processing jobs
        queue.testMode.enter();

        // Call the function
        createPushNotificationsJobs(queue);

        // Check if the correct jobs are added to the queue
        expect(queue.testMode.jobs.length).to.equal(1); // Modify as per your expected number of jobs
        const job = queue.testMode.jobs[0];
        expect(job.type).to.equal('push notification');
        // You can add more assertions based on the job properties set by createPushNotificationsJobs

        // Exit test mode (process the jobs)
        queue.testMode.exit();
    });

});

