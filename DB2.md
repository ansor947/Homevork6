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
 