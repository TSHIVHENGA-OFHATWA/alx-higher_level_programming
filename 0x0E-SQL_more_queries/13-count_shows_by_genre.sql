-- This script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(show_id) AS number_of_shows
FROM tv_genre JOIN tv_show_genre ON tv_genre.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;