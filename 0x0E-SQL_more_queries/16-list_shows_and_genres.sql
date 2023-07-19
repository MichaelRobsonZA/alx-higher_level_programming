-- 16. List shows and genres
SELECT tv_shows.title, GROUP_CONCAT(genres.name ORDER BY genres.name ASC SEPARATOR ', ') AS 'genres' FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id JOIN genres ON tv_show_genres.genre_id = genres.id GROUP BY tv_shows.id ORDER BY tv_shows.title ASC;
