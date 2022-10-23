INSERT INTO genre (title)
	VALUES
	('country'),
	('blues'),
	('jazz'),
	('hip hop'),
	('rock');

INSERT INTO musician (names)
	VALUES
	('Taylor Swift'),
	('Eagles'),
	('Louis Armstrong'),
	('Frank Sinatra'),
	('Eric Clapton'),
	('50 Cent'),
	('ДДТ'),
	('Би-2');

INSERT INTO track(track_name, duration)
	VALUES
	('Tell Me Why', '00:03:56'),
	('Fifteen', '00:03:26'),
	('Hotel California', '00:03:41'),
	('What a Wonderful World', '00:02:01'),
	('What Now My Love', '00:05:59'),
	('Somewhere My Love', '00:04:12'),
	('Hey Hey', '00:02:19'),
	('Running on Faith', '00:05:42'),
	('Follow My Lead', '00:03:12'),
	('My Gun Goo', '00:05:30'),
	('Ты не один', '00:03:25'),
	('Дождь', '00:02:51'),
	('Мой рок-н-ролл', '00:05:33'),
	('Чёрное солнце', '00:06:01'),
	('Детство', '00:03:05');

INSERT INTO collection(title_collection, year_of_realise)
	VALUES
	('country music', '2018-11-25'),
	('blue devils', '2019-02-28'),
	('blues collection', '2019-03-08'),
	('jazz collection', '2000-10-17'),
	('jazz volume 1', '2003-01-28'),
	('jazz the best', '2014-07-09'),
	('hip hop music', '2020-12-26'),
	('rock collection', '2018-03-25');
	
INSERT INTO album(title_album, year_of_realise)
	VALUES
	('Fearless', '2008-10-24'),
	('Hotel California', '1976-12-2'),
	('What A Wonderful World', '1988-07-06'),
	('That"s Life', '1966-03-18'),
	('Unplugged', '1992-01-10'),
	('Curtis', '2007-09-03'),
	('Просвистела', '1999-12-30'),
	('Горизонт событий', '2017-08-23');

-- Здравствуйте,
-- после ввода данных заполняются лишь указанные таблицы,
-- промежуточные остаются без значений. Не пойму, почему?
-- Так и должно быть или я должет заполнять их с помощью
-- подобных команд? В чем тогда смысл привязки ключей?
-- Скорее всего я что-то делаю не так, но что?

