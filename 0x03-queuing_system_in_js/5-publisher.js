// Import Redis client library
import { createClient } from 'redis';
const redis = require('redis');

// Create a Redis client
const client = createClient()
  client.on('error', err => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

// Function to publish a message after a certain time
function publishMessage(message, time) {
  setTimeout(() => {
    console.log('About to send ', message);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
