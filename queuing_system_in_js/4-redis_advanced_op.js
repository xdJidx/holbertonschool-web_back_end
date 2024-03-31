import redis from 'redis';

const client = redis.createClient();

// Gestion des erreurs de connexion
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Création du hash
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Affichage du hash
client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
        console.error('Error getting hash:', err);
    } else {
        console.log('Hash stored in Redis:', reply);
    }
});
