import psycopg2  

password = '230611End'

with psycopg2.connect(database = 'HomeWork', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

    with conn.cursor() as cur:

            cur.execute("""
                        DROP TABLE clients_numbers;
                        DROP TABLE clients;
                        """)
            conn.commit()
            print('Success')
#  DROP TABLE clients_numbers;

    cur.close() 
conn.close()


# import psycopg2  

# password = '230611End'

# with psycopg2.connect(database = 'Tips', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

#     with conn.cursor() as cur:
        
#             cur.execute("""
#                         DROP TABLE clients_numbers;
#                         DROP TABLE clients;
#                         """)
#             conn.commit()
#             print('Success')


#     cur.close() 
# conn.close()

# CREATE TABLE IF NOT EXISTS 
# clients(
# id SERIAL PRIMARY KEY,
# name VARCHAR(80) UNIQUE NOT NULL,
# surname VARCHAR(80) UNIQUE NOT NULL,
# email VARCHAR(80) UNIQUE NOT NULL);

# CREATE TABLE IF NOT EXISTS clients_numbers(
# id SERIAL PRIMARY KEY,
# clients_id INTEGER REFERENCES clients(id),
# number BIGINT UNIQUE NOT NULL);

        
# INSERT INTO clients(name, surname, email) 
# VALUES
# ('Сидор', 'Сидоров', 'sidorov@yandex.ru'),
# ('Иван', 'Иванов', 'ivanov@yandex.ru');

# INSERT INTO clients_numbers(number)
# VALUES
# (89275486328),
# (89157469821);

# UPDATE clients 
# SET name = 'Василий', surname = 'Васильев', email = 'vasiliev@yandex.ru' 
# WHERE id = 2;