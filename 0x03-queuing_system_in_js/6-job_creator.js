const kue = require('kue');
const queue = kue.createQueue();

// Define the object conatining the jobData
const jobData =  {
    phoneNumber: '+234 786 908 909',
    message: 'With practice, your coding only gets better'
};

//Create a job and add it to a queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
     if (!err) {
       console.log(`Notification job created: ${job.id}`);
     } else {
       console.error('Error creating job:', err);
     }
});

// When job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// When job is failing
job.on('failed', () => {
  console.log('Notification job failed');
});
