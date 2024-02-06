// Import Redis client library
import { createClient } from 'redis';
import { promisify } from 'util';
const redis = require('redis');

// Create a Redis client
const client = createClient()
  client.on('error', err => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the get method of the redis client
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
      const value = await getAsync(schoolName);
      console.log(`Value for ${schoolName}: ${value}`);
    } catch (error) {
      console.error('Error:', error);
    }
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
