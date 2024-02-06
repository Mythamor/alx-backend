const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in queue
queue.process('push_notification_code', (job, done) => {
  // Extract phone n. and message from job data
  const { phoneNumber, message } = job.data;

  // Call the function
  sendNotification(phoneNumber, message);

 done();
});

// Log message when a job is completed
queue.on('job complete', (id) => {
  console.log(`Job ${id} is completed`)
});
