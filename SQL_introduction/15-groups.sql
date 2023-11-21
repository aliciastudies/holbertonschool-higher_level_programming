-- lists number of records with the same score in table etc
SELECT score, COUNT(score) FROM second_table
GROUP BY score;