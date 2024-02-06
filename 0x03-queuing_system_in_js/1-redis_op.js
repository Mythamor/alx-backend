// Import Redis client library
import { createClient } from 'redis';
const redis = require('redis');

// Create a Redis client
const client = createClient()
  client.on('error', err => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, res) => {

    if (err) {
      console.error('Error setting key:', err);
    } else {
      console.log('Key set successfully:', res);
    }
  });
}

// 
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
