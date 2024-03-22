-- Create a function that takes two integers and returns a float.
-- If the second integer is 0, the function should return 0.
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    RETURN result;
END//
DELIMITER ;
