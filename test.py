import psycopg2  

def create_db(conn):

    cur.execute("""
                CREATE TABLE IF NOT EXISTS genre(
                id SERIAL PRIMARY KEY,
                title VARCHAR (60) UNIQUE NOT NULL);
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS musician(
                id SERIAL PRIMARY KEY,
                names VARCHAR(80) UNIQUE NOT NULL );
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS album(
                id SERIAL PRIMARY KEY,
                title_album VARCHAR (60) UNIQUE NOT NULL,
                year_of_realise DATE NOT NULL);
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS collection(
                id SERIAL PRIMARY KEY,
                title_collection VARCHAR (60) UNIQUE NOT NULL,
                year_of_collection DATE NOT NULL);
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS track(
                id SERIAL PRIMARY KEY,
                track_name VARCHAR (60) UNIQUE NOT NULL,
                album_id INTEGER REFERENCES album(id),
                duration TIME);
                """)

def create_dop(conn):

    cur.execute("""
                CREATE TABLE IF NOT EXISTS collections_tracks(
                id SERIAL PRIMARY KEY,
                track_id INTEGER NOT NULL REFERENCES track(id),
                collection_id INTEGER NOT NULL REFERENCES collection(id)); 
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS genres_musicians(
                id SERIAL PRIMARY KEY,
                genre_id INTEGER NOT NULL REFERENCES genre(id),
                musician_id INTEGER NOT NULL REFERENCES musician(id));

                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS album_musicians(
                id SERIAL PRIMARY KEY,
                album_id INTEGER NOT NULL REFERENCES album(id),
                musician_id INTEGER NOT NULL REFERENCES musician(id));
                """)


def insert(conn):

    cur.execute("""
                INSERT INTO genre (title)
                VALUES
                ('country'),
                ('blues'),
                ('jazz'),
                ('hip hop'),
                ('rock');
                """)

    cur.execute("""
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
                """)

    cur.execute("""
                INSERT INTO album(title_album, year_of_realise)
                VALUES
                ('Fearless', '2020-10-24'),
                ('Hotel California', '1976-12-2'),
                ('What A Wonderful World', '1988-07-06'),
                ('That"s Life', '1966-03-18'),
                ('Unplugged', '1992-01-10'),
                ('Curtis', '2007-09-03'),
                ('Просвистела', '1999-12-30'),
                ('Горизонт событий', '2019-08-23');
                """)

    cur.execute("""
                INSERT INTO collection(title_collection, year_of_collection)
                VALUES
                ('country music', '2018-11-25'),
                ('blue devils', '2019-02-28'),
                ('blues collection', '2019-03-08'),
                ('jazz collection', '2000-10-17'),
                ('jazz volume 1', '2003-01-28'),
                ('jazz the best', '2014-07-09'),
                ('hip hop music', '2020-12-26'),
                ('rock collection', '2018-03-25');
                """)

    cur.execute("""
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
                """)

password = '230611End'



with psycopg2.connect(database = 'Tips', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

    with conn.cursor() as cur:

        create_db(conn)
        conn.commit()

        insert(conn)
        conn.commit()

        create_dop(conn)
        conn.commit()

        print('Success')



    cur.close() 
conn.close()