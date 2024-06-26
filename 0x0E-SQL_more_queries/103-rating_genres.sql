-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.ID = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
