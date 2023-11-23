-- lists all cities of state found in database
SELECT id, name from cities
WHERE state_id = 1
ORDER BY cities.id ASC;