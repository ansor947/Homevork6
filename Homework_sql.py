# Здесь описал логику ДЗ, как я ее понял. Не совсем ясно, нужна ли практическая реализация или лишь понимание. На всякий случай,
#     во втором файле пример реализации.

import psycopg2

def create_connection(database, user, password):
    conn = psycopg2.connect(database = 'homework', user = 'postgres', password = '230611End')
    return conn   

def create_cursor(conn):
    cur = conn.cursor
    return cur


# Функция, создающая структуру БД (таблицы)

    def clients_base():
        create_cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) UNIQUE NOT NULL,
            surname VARCHAR(40) UNIQUE NOT NULL,
            email VARCHAR(40) UNIQUE NOT NULL);
            """)
        create_connection.commit()
        

    def number_clients_base():
        create_cursor.execute("""CREATE TABLE IF NOT EXISTS clients_numbers(
            id SERIAL PRIMARY KEY,
            clients_id INTEGER NOT NULL REFERENCES clients(id),
            number INTEGER NOT NULL);
            """)
        create_connection.commit()

# Функция, позволяющая добавить нового клиента

    def new_client(name, surname, email):
        create_cursor.execute("""INSERT INTO
            name(),
            surname(),
            email();
            """)
        create_connection.commit()

# Функция, позволяющая добавить телефон для существующего клиента

    def new_number(number):
        create_cursor.execute("""INSERT INTO number();
        """)
        create_connection.commit()

# Функция, позволяющая изменить данные о клиенте

    def update_client(name, surname, email):
        create_cursor.execute("""UPDATE clients 
            SET name=%s, surname=%s, email=%s 
            WHERE id=%s;
            """)
        create_connection.commit()

# Функция, позволяющая изменить номер телефона клиента

    def update_number(number):
        create_cursor.execute("""UPDATE clients_numbers SET 
            number=%s,
            WHERE id=%s;
            """)
        create_connection.commit()

# Функция, позволяющая удалить существующего клиента

    def delete_client(name, surname, email):
        create_cursor.execute("""DELETE FROM clients 
            SET name=%s, surname=%s, email=%s 
            WHERE id=%s;
            """)
        create_connection.commit()

# Функция, позволяющая удалить телефон для существующего клиента

    def delete_number(number):
        create_cursor.execute("""DELETE FROM clients_numbers SET 
            number=%s,
            WHERE id=%s;
            """)
        create_connection.commit()

# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

    def get_clients_date(cursor, name:str,  surname:str, email:str, number:int) -> int:
            create_cursor.execute("""
            SELECT name, surname, email, number FROM clients
            JOIN clients_numbers
            WHERE name=%s or surname=%s or email=%s or number=%s;
            """)       

create_connection.close()











# def get_course_id(cursor, name: str) -> int:
#             cursor.execute("""
#             SELECT id FROM course WHERE name=%s;
#             """, (name,))
#             return cur.fetchone()[0]
#         python_id = get_course_id(cur, 'Python')
#         print('python_id', python_id)







# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)