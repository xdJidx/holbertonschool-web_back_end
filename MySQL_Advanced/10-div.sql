-- Create a function that takes two integers and returns a float.
-- If the second integer is 0, the function should return 0.
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
    DECLARE result FLOAT;
    
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = ROUND(a / b, 6);
    END IF;
    
    RETURN result;
END;
//

DELIMITER ;
