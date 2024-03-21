-- Create a stored procedure named `ComputeAverageScoreForUser` 
-- that takes a user_id as input and computes the average score for that user.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_corrections INT;
    DECLARE current_average FLOAT;

    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate total number of corrections for the user
    SELECT COUNT(*) INTO total_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate current average score for the user
    SELECT average_score INTO current_average
    FROM users
    WHERE id = user_id;

    -- Compute new average score
    IF total_corrections > 0 THEN
        IF total_corrections = 1 THEN
            -- If it's the first correction, just set the average to the score
            UPDATE users
            SET average_score = total_score
            WHERE id = user_id;
        ELSE
            -- Otherwise, update the average by taking into account the previous average and the new score
            UPDATE users
            SET average_score = (current_average * (total_corrections - 1) + total_score) / total_corrections
            WHERE id = user_id;
        END IF;
    ELSE
        -- If there are no corrections, set the average to 0
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;
