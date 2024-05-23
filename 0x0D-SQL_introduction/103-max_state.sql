-- displays the max temperature of each state(ordered by State name)
-- displays the max value of a column in a table
SELECT state, MAX(temperature) AS max_temperature
FROM cities
GROUP BY state
ORDER BY state;
