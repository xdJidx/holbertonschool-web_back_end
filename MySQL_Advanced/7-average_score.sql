-- Stored procedure to compute and store the average score for a student
-- Input: user_id, a users.id value
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = users.id
    )
    WHERE users.id = user_id;
END//
DELIMITER ;
