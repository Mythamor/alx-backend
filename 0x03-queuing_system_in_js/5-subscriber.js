// Import Redis client library
import { createClient } from 'redis';
const redis = require('redis');

// Create a Redis client
const client = createClient()
  client.on('error', err => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

// Subscribe to the channel
client.subscribe('holberton school channel');

// On message
client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
