-- 13. Number of shows by genre
SELECT genres.name, COUNT(tv_shows.id) AS 'number_of_shows' FROM genres LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id GROUP BY genres.id ORDER BY genres.name ASC;
