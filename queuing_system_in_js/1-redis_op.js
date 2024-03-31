import redis from 'redis';

// Création du client Redis
const client = redis.createClient();

// Gestion des erreurs de connexion
client.on('error', (error) => {
    console.error('Redis client not connected to the server:', error);
});

// Connexion au serveur Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Fonction pour définir une nouvelle école dans Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Fonction pour afficher la valeur d'une école dans Redis
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) {
            console.error('Error getting value:', error);
        } else {
            console.log(value);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
