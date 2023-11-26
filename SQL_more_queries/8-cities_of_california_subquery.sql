-- lists all cities of state found in database
SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY id ASC;