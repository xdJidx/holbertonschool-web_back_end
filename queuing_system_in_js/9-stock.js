const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Create Express app
const app = express();
const PORT = 1245;

// Sample data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Redis client
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);

// Data access functions
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Server routes

// Route to get list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  })));
});

// Route to get details of a specific product
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  
  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: "Product not found" });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity >= product.stock) {
    return res.json({ status: "Not enough stock available", itemId: product.id });
  }

  // Reserve one item
  reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: "Reservation confirmed", itemId: product.id });
});

// Reserve stock in Redis
function reserveStockById(itemId, stock) {
  redisClient.set(`item.${itemId}`, stock);
}

// Get current reserved stock from Redis
async function getCurrentReservedStockById(itemId) {
  const value = await getAsync(`item.${itemId}`);
  return parseInt(value) || 0;
}

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
