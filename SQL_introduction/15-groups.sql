-- lists number of records with the same score in table etc
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;