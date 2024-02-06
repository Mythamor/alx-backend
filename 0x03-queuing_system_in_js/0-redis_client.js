import { createClient } from 'redis';

const client = createClient()
  client.on('error', err => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

client.set('key', 'value', (err, res) => {
  if (err) {
    console.error('Error setting key:', err);
  } else {
    console.log('Key set successfully:', res);
 }
});
