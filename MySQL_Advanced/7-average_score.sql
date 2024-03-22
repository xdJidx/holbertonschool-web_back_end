-- Create a stored procedure named `ComputeAverageScoreForUser` 
-- that takes a user_id as input and computes the average score for that user.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT) -- Paramètre d'entrée représentant l'identifiant de l'utilisateur
BEGIN
    -- Déclaration d'une variable pr stocker la moyenne des scores
    DECLARE avg_score FLOAT;

    -- Calcul de la moyenne des scores pour l'utilisateur spécifié
    SET avg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);

    -- Update de la colonne average_score dans la table users avec la moyenne calculée
    UPDATE users SET average_score = avg_score WHERE id=user_id;
END

END;
//
DELIMITER ;
