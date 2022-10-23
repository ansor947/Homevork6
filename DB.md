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

Так и не смог понять, что ставить в промежуточных таблицах: PK или FK? Поставил PK. Хотя меня смущает REFERENCES в коде, 
которы, как следует из леции подразумевает собой FK.
    
