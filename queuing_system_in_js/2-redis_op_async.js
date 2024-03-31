import redis from 'redis';

const client = redis.createClient();
const { promisify } = require('util');

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Fonction asynchrone pour afficher la valeur d'une école dans Redis
async function displaySchoolValue(schoolName) {
    // Promisification de la fonction client.get et liaison du contexte
    const getasync = promisify(client.get).bind(client);
    // Appel asynchrone de la fonction promisifiée pour récupérer la valeur de l'école
    const value = await getasync(schoolName);
    // Affichage de la valeur de l'école
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');