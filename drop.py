import psycopg2  

password = '230611End'

with psycopg2.connect(database = 'HomeWork', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

    with conn.cursor() as cur:

            cur.execute("""

                        DROP  TABLE clients_numbers;
                        DROP TABLE clients;
                        """)
                        
            print('Success')

    cur.close() 
conn.close()