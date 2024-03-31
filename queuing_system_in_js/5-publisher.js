import redis from 'redis';

// Créer un client Redis pour le publisher
const publisher = redis.createClient();

// Gestion des erreurs de connexion
publisher.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Fonction pr publier un message avec un délai
function publishMessage(message, time) {
    // Définir un délai pour l'envoi du message
    setTimeout(() => {
        // Afficher le message à envoyer
        console.log(`About to send ${message}`);
        // Publier le message sur le canal "holberton school channel"
        publisher.publish('holberton school channel', message);
    }, time);
}

// Publier plusieurs messages avec différents délais
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300); // Envoyer un message pour tuer le serveur
publishMessage("Holberton Student #3 starts course", 400);
