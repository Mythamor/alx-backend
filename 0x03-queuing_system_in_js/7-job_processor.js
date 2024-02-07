const kue = require('kue')
const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0);

  // Check if the number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed(errorMessage);
    done(new Error(errorMessage));
  } else {
   // Update progress to 50%
   job.progress(50);

  // Log  the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
 
  // Call done to iindicate the completion of the job
  done();
  }
}

// Configure the Kue queue that processes the jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
