-- Здравствуйте, 
-- написал 2 варианта, так как не понимаю, что подойдет лучше. 
-- Если можете, подскажите какой и почему?

-- https://drive.google.com/file/d/15xs5DW2d7VTGY3UFziJsLGE5S0lRt0td/view?usp=sharing
-- таблицу обновил согласно рекомендации


CREATE TABLE IF NOT EXISTS genre(
    genre_id VARCHAR(40) PRIMARY KEY,
    title VARCHAR (60) NOT NULL
    );

CREATE TABLE IF NOT EXISTS musician(
    musician_id VARCHAR(60) PRIMARY KEY,
    names VARCHAR(80) NOT NULL 
    );

CREATE TABLE IF NOT EXISTS genres_musicians(
    genre_id VARCHAR(40) REFERENCES genre(genre_id),
    musician_id VARCHAR(60) REFERENCES musician(musician_id),
    CONSTRAINT gm PRIMARY KEY(genre_id, musician_id)
    );

CREATE TABLE IF NOT EXISTS album(
    album_id VARCHAR(40) PRIMARY KEY,
    title_album VARCHAR (60) NOT NULL,
    year_of_realise DATE NOT NULL
    );

CREATE TABLE IF NOT EXISTS album_musicians(
    album_id VARCHAR(40) REFERENCES album(album_id),
    musician_id VARCHAR(60) REFERENCES musician(musician_id),
    CONSTRAINT am PRIMARY KEY(album_id, musician_id)
    );

CREATE TABLE IF NOT EXISTS collection(
    collection_id VARCHAR(40) PRIMARY KEY,
    title_collection VARCHAR (60) NOT NULL,
    year_of_realise DATE NOT NULL
    );

CREATE TABLE IF NOT EXISTS track(
    track_id VARCHAR(40) PRIMARY KEY,
    album_id VARCHAR (60) NOT NULL UNIQUE REFERENCES album(album_id),
    duration TIME,
    collection_id VARCHAR (60) REFERENCES collection(collection_id)
    );

CREATE TABLE IF NOT EXISTS collections_tracks(
    track_id VARCHAR(40) REFERENCES album(track_id),
    collection_id VARCHAR(60) REFERENCES musician(collection_id),
    CONSTRAINT am PRIMARY KEY(track_id, collection_id)
    );

    -----------------------------------------------------------

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
    duration TIME,
    collection_id INTEGER REFERENCES collection(id)
    );

CREATE TABLE IF NOT EXISTS collections_tracks(
    id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES album(id),
    collection_id INTEGER REFERENCES musician(id)
    );    