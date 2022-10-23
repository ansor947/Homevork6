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