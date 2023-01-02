# import psycopg2  

# password = '230611End'

# with psycopg2.connect(database = 'HomeWork', user = 'postgres', password = password, host = 'localhost', port = '5432') as conn:

#     with conn.cursor() as cur:




        

        # cur.execute("""
        #     DROP TABLE clients_numbers;
        #     DROP TABLE clients;
        #     """)

            # Функция, создающая структуру БД (таблицы)

        # def clients_base():
        #     cur.execute("""
        #                 CREATE TABLE IF NOT EXISTS clients(
        #                 id SERIAL PRIMARY KEY,
        #                 name VARCHAR(80) UNIQUE NOT NULL,
        #                 surname VARCHAR(80) UNIQUE NOT NULL,
        #                 email VARCHAR(80) UNIQUE NOT NULL);
        #                 """)    
        #     conn.commit()
        # clients_base()
        # conn.commit()

        # def number_clients_base():
        #     cur.execute("""
        #                 CREATE TABLE IF NOT EXISTS clients_numbers(
        #                 id SERIAL PRIMARY KEY,
        #                 clients_id INTEGER REFERENCES clients(id),
        #                 number BIGINT UNIQUE NOT NULL);
        #                 """)
        #     conn.commit()
        # number_clients_base()
        # conn.commit()

        #     # Функция, позволяющая добавить нового клиента

        # def new_client(): 
        #     cur.execute("""
        #                 INSERT INTO clients(name, surname, email) 
        #                 VALUES
        #                 ('Сидор', 'Сидоров', 'sidorov@yandex.ru'),
        #                 ('Иван', 'Иванов', 'ivanov@yandex.ru');
        #                 """)
        #     conn.commit()

        # new_client()
        # conn.commit()

        #         # Функция, позволяющая добавить телефон для существующего клиента

        # def new_number():
        #     cur.execute("""
        #                 INSERT INTO clients_numbers(number)
        #                 VALUES
        #                 (89275486328),
        #                 (89157469821);
        #                 """)
        #     conn.commit()

        # new_number()
        # conn.commit()

        # def update_client():
        #     cur.execute("""
        #                 UPDATE clients 
        #                 SET name = 'Василий', surname = 'Васильев', email = 'vasiliev@yandex.ru' 
        #                 WHERE id = 2;
        #                 """, )
        #     conn.commit()

        # update_client()
        # conn.commit()

        # def update_number():
        #     cur.execute("""
        #                 UPDATE clients_numbers 
        #                 SET number = 89196542398
        #                 WHERE id = 2;
        #                 """)
        #     conn.commit()

        # update_number()
        # conn.commit()

        # def delete_client():
        #     cur.execute("""
        #                 DELETE FROM clients 
        #                 WHERE id = 2;
        #                 """)
        #     conn.commit()

        # delete_client()
        # conn.commit()

        # def delete_number():
        #     cur.execute("""
        #                 DELETE number FROM clients_numbers 
        #                 WHERE id = 1;
        #                 """)
        #     conn.commit()

        # delete_number()
        # conn.commit()

        # def get_clients_date():
        #     cur.execute("""
        #                 SELECT name, surname FROM clients
        #                 WHERE name = 'Сидор';
        #                 """)
        #     return cur.fetchall()


        # def get_course_id(cursor, name: str) -> int:
        #     cursor.execute("""
        #     SELECT id FROM course WHERE name=%s;
        #     """, (name,))
        #     return cur.fetchone()[0]
        # python_id = get_course_id(cur, 'Python')
        # print('python_id', python_id)
        
#         conn.commit()
#         print('Success')


#     cur.close() 
# conn.close() 

        # cur.execute("""SELEKT * FROM clients_base();
        #             """)

# print('fetchall',clients_base())