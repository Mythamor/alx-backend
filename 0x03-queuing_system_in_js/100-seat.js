const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

// Create Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Set the initial number of available seats to 50
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// Get the current number of available seats
async function getCurrentAvailableSeats() {
    const availableSeats = await getAsync('available_seats');
    return parseInt(availableSeats);
}

// Initialize reservation status
let reservationEnabled = true;

// Create a Kue queue
const queue = kue.createQueue();

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
        return;
    }

    // Create and queue a job
    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            res.json({ status: 'Reservation failed' });
        } else {
            res.json({ status: 'Reservation in process' });
        }
    });
});

// Route to process the queue and decrease available seats
app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });

    // Process the queue reserve_seat
    queue.process('reserve_seat', async (job, done) => {
        let availableSeats = await getCurrentAvailableSeats();
        if (availableSeats === 0) {
            reservationEnabled = false;
            done(new Error('Not enough seats available'));
        } else {
            availableSeats -= 1;
            await reserveSeat(availableSeats);
            if (availableSeats === 0) {
                reservationEnabled = false;
            }
            console.log(`Seat reservation job ${job.id} completed`);
            done();
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

