-- Create a view called need_meeting that shows the names of students
-- who need to meet with their advisor.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
