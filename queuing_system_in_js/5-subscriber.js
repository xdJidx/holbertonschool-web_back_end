import redis from 'redis';

const subscriber = redis.createClient();

// Gestion des erreurs de connexion
subscriber.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Souscripteur abonné à un canal
subscriber.subscribe('holberton school channel');
// Écoute des messages publiés sur le canal
subscriber.on('message', (channel, message) => {
    console.log(`Received message from channel ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        console.log('Unsubscribing and quitting...');
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
