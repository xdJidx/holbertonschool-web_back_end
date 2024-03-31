import redis from 'redis';

// Créez un client Redis
const client = redis.createClient();

// Connexion au serveur Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Géstion des erreurs de connexion
client.on('error', (error) => {
    console.error('Redis client not connected to the server:', error);
});
