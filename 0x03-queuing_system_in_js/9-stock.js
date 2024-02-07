const express = require('express');
const { promisify } = require('util');
const redis = require('redis');

// Set up express server
const app = express();
const PORT = 1245;

// Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


// Array of products
const listProducts = [
       {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
       {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
       {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
       {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
];


// Function to et item by id
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}


// Function to reserve stock by ID
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}


// Function to get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}


// Route to get list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => (
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  )));
});


// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product) {
        res.json({ status: 'Product not found' });
    } else {
        const currentQuantity = product.stock - await getCurrentReservedStockById(itemId);
        res.json({
            itemId: product.id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock,
            currentQuantity: currentQuantity
        });
    }
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product) {
        res.json({ status: 'Product not found' });
    } else {
        const currentReservedStock = await getCurrentReservedStockById(itemId);
        if (currentReservedStock >= product.stock) {
            res.json({ status: 'Not enough stock available', itemId: itemId });
        } else {
            await reserveStockById(itemId, currentReservedStock + 1);
            res.json({ status: 'Reservation confirmed', itemId: itemId });
        }


// Start the server
app.listen(port, () => {
  console.log(`Server is running on PORT ${PORT}`);
});
