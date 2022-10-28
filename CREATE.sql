-- https://drive.google.com/file/d/15xs5DW2d7VTGY3UFziJsLGE5S0lRt0td/view?usp=sharing 
-- ссылка на диаграмму

CREATE TABLE IF NOT EXISTS genre(
    id SERIAL PRIMARY KEY,
    title VARCHAR (60) UNIQUE NOT NULL
    );

CREATE TABLE IF NOT EXISTS musician(
    id SERIAL PRIMARY KEY,
    names VARCHAR(80) UNIQUE NOT NULL 
    );

CREATE TABLE IF NOT EXISTS genres_musicians(
    id SERIAL PRIMARY KEY,
    genre_id INTEGER REFERENCES genre(id),
    musician_id INTEGER REFERENCES musician(id)
    );

CREATE TABLE IF NOT EXISTS album(
    id SERIAL PRIMARY KEY,
    title_album VARCHAR (60) UNIQUE NOT NULL,
    year_of_realise DATE NOT NULL
    );

CREATE TABLE IF NOT EXISTS album_musicians(
    id SERIAL PRIMARY KEY,
    album_id INTEGER REFERENCES album(id),
    musician_id INTEGER REFERENCES musician(id)
    );

CREATE TABLE IF NOT EXISTS collection(
    id SERIAL PRIMARY KEY,
    title_collection VARCHAR (60) NOT NULL,
    year_of_realise DATE NOT NULL
    );

CREATE TABLE IF NOT EXISTS track(
    id SERIAL PRIMARY KEY,
    track_name VARCHAR (60) NOT NULL,
    album_id INTEGER REFERENCES album(id),
    duration NUMERIC(3,2)
    );

CREATE TABLE IF NOT EXISTS collections_tracks(
    id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES album(id),
    collection_id INTEGER REFERENCES musician(id)
    );    

Не могу понять как внести в таблицу данные NUMERIC. Прописал (3,2). Но получаю ошибку, 
хотя из логики и найденного мной в интернете все верно должно быть. Постановка "," непомогает.
Помогите, пожалуйста, понять как правильно должны быть прописаны данные при внесении!



INSERT INTO track(track_name, duration)
	VALUES
	('Tell Me Why', '356'),
	('Fifteen', '326'),
	('Hotel California', '341'),
	('What a Wonderful World', '201'),
	('What Now My Love', '559'),
	('Somewhere My Love', '412'),
	('Hey Hey', '219'),
	('Running on Faith', '542'),
	('Follow My Lead', '312'),
	('My Gun Goo', '530'),
	('Ты не один', '325'),
	('Дождь', '251'),
	('Мой рок-н-ролл', '533'),
	('Чёрное солнце', '601'),
	('Детство', '305');

