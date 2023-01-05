import psycopg2  

password = '230611End'

with psycopg2.connect(database = 'Tips', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

    with conn.cursor() as cur:

            cur.execute("""

                        DROP  TABLE  genre CASCADE ;
                        DROP TABLE  musician CASCADE ;
                        DROP TABLE  album CASCADE ;
                        DROP TABLE collection CASCADE ;
                        DROP TABLE  track CASCADE ;
                        DROP TABLE  genres_musicians;
                        DROP TABLE  album_musicians;
                        DROP TABLE collections_tracks;
                        """)
            conn.commit()
            print('Success')

    cur.close() 
conn.close()