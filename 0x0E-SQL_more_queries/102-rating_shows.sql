-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, SUM(tv_shows.rating) AS rating_sum
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
