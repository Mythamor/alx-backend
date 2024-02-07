const kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  
  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData);
    
    job.save((err) => {
    // Log when job is created
      if ( !err ) {
	console.log(`Notification job created: ${job.id}`);
      }
     });

    // Log when job is complete
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    // Log when job failed
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Log when job is making progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    
  });
}

export default createPushNotificationsJobs;
