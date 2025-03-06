-- get the score which are not null from a table
-- order them by descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;