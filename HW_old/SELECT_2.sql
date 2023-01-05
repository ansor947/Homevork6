-- количество исполнителей в каждом жанре;

SELECT title, COUNT(names) FROM  genre g
	JOIN genres_musicians gm ON g.id = gm.genre_id
	JOIN musician m ON m.id = g.id 
    GROUP BY g.title
    ORDER by title;  

-- количество треков, вошедших в альбомы 2019-2020 годов;

SELECT COUNT(DISTINCT track_name) FROM track t
	JOIN album a ON t.album_id = a.id
    WHERE year_of_realise BETWEEN '2019-01-01' AND '2021-01-01';


-- средняя продолжительность треков по каждому альбому;

SELECT title_album, AVG(duration) FROM album a
    JOIN track t ON t.album_id = a.id
    GROUP BY a.title_album
    ORDER by AVG(duration);

-- все исполнители, которые не выпустили альбомы в 2020 году;

SELECT names FROM musician m
    JOIN album_musicians am ON am.musician_id = m.id 
	JOIN album a ON am.album_id = a.id
	WHERE year_of_realise NOT BETWEEN '2020-01-01' AND '2021-12-31';

-- названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

SELECT DISTINCT title_collection, names FROM  collection c
	JOIN collections_tracks ct ON ct.collection_id = c.id
	JOIN track t ON ct.track_id = t.id
    JOIN album a ON t.album_id = a.id
    JOIN album_musicians am ON am.album_id = a.id
    JOIN musician m ON am.musician_id = m.id
    WHERE names = 'Taylor Swift'; 

-- название альбомов, в которых присутствуют исполнители более 1 жанра;

SELECT title_album FROM album a 
	JOIN album_musicians am ON am.album_id = a.id
	JOIN musician m ON am.musician_id = m.id
	JOIN genres_musicians gm ON gm.musician_id = m.id
	JOIN genre g ON gm.genre_id = g.id
	GROUP BY a.title_album
	HAVING COUNT(genre_id) > 1;

-- наименование треков, которые не входят в сборники;

SELECT track_name FROM track t
	LEFT JOIN collections_tracks ct ON ct.track_id = t.id
    LEFT JOIN collection c ON ct.collection_id = c.id
    GROUP BY t.track_name
    HAVING COUNT(track_id) = 0;

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек 
-- (теоретически таких треков может быть несколько);

SELECT names, duration FROM musician m
    JOIN album_musicians am ON am.musician_id = m.id
    JOIN album a ON am.album_id = a.id
    JOIN track t ON t.album_id = a.id
    WHERE duration = (SELECT MIN(duration) FROM track);

-- название альбомов, содержащих наименьшее количество треков.

WITH link_counts AS (SELECT title_album, COUNT(album_id) as num_links
        FROM album a
        JOIN track t ON a.id = t.album_id
        GROUP BY title_album)                     
SELECT title_album FROM link_counts
WHERE num_links = (SELECT MIN(num_links) FROM link_counts);


    ##################### Старые запросы ######################


SELECT title_album, year_of_realise FROM album
    WHERE DATE(year_of_realise) >= '2000-01-01';

SELECT track_name, duration FROM track
    WHERE id > 0 ORDER BY duration DESC LIMIT 1;


SELECT track_name, duration FROM track
    WHERE duration >= '00:03:30';

SELECT title_collection FROM collection
    WHERE year_of_realise BETWEEN '2018-01-01' AND '2020-01-01';

SELECT names FROM musician
    WHERE names NOT LIKE '% %';

SELECT track_name FROM track
    WHERE track_name LIKE '%Мой%' OR track_name LIKE '%My%';