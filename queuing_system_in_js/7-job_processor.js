const kue = require('kue');

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    // Suivi de la progression du travail
    job.progress(0, 100);

    // Vérification si le numéro de téléphone est dans la liste noire
    if (blacklistedNumbers.includes(phoneNumber)) {
        // Échec du travail avec un message d'erreur
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Suivi de la progression du travail
    job.progress(50, 100);

    // Envoi de la notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simuler un délai pour l'envoi de la notification (à des fins de démonstration)
    setTimeout(() => {
        // Mise à jour de la progression du travail
        job.progress(100, 100);
        // Fin du travail avec succès
        done();
    }, 2000); // Temps de délai de 2 secondes pour l'envoi de la notification
}

// Processus de traitement des travaux de la file d'attente
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    // Appel de la fonction sendNotification pour gérer le travail
    sendNotification(phoneNumber, message, job, (error) => {
        if (error) {
            // Gestion de l'erreur si le travail échoue
            console.error(`Notification job ${job.id} failed: ${error.message}`);
        } else {
            // Fin du travail avec succès
            console.log(`Notification job ${job.id} completed`);
        }
        // Indiquer que le travail est terminé
        done(error);
    });

    // Écouteur d'événement pour mettre à jour la progression du travail
    job.on('progress', (progress) => {
        // Affichage du pourcentage de progression
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
});
