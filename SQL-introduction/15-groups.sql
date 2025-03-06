-- get the number of score
-- that are the same
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;