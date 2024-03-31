const kue = require('kue');

// Création de la file d'attente
const queue = kue.createQueue();

// Données de la tâche à créer
const jobData = {
    phoneNumber: '1234567890',
    message: 'Samsam', 
};

// Création et save de la tâche dans la queue
const job = queue.create('push_notification_code', jobData).save((err) => {
    // Gestion des erreurs lors de la création de la tâche
    if (err) {
        console.error('Notification job failed:', err);
    } else {
        // Affichage de l'ID de la tâche créée
        console.log('Notification job created:', job.id); 
    }
});

// Traitement de la tâche lorsqu'elle est en cours
queue.process('push_notification_code', (job, done) => {
    // Traitement de la tâche ici
    console.log('Notification job completed'); 
    done(); // Indication que le traitement de la tâche est terminé
});
