const redis = require('redis');
const client = redis.createClient();


// Function to create a hash and store the values
function createHash() {
  client.HSET('HolbertonSchools','Portland', '50', redis.print);
  client.HSET('HolbertonSchools','Seattle', '80', redis.print);
  client.HSET('HolbertonSchools','New York', '20', redis.print);
  client.HSET('HolbertonSchools','Bogota', '20', redis.print);
  client.HSET('HolbertonSchools','Cali', '40', redis.print);
  client.HSET('HolbertonSchools','Paris', '2', redis.print);
}

// Function to display the hash
function displayHash() {
  client.hgetall('HolbertonSchools', (err, res) => {
    if (err) {
      console.error('Error:', err);
    } else {
        console.log('Hash values:', res)
    }
  });
}

// Call the display function
createHash();

// Call the displayHash function after a delay to ensure hash is created
setTimeout(displayHash, 1000);
