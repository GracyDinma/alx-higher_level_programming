-- lists all show contained in hbtn_od_tvshows
-- that have at least one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascendind order by tv_shows.title and
-- tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genre.genre_id ASC;
