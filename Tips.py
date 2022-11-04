# С реализацией все не так гладко. По какой-то причине при взаимодействии VSC с sql - все глючит. 
#     Таблицы создаются через раз, хотя код в DBeaver работает исправно. По этой причине реализовал cjnnect и 
#     через глобальную переменную, а cursor пришлось интегрировать в каждую функцию, иначе ловил ошибки. Даже .json стал 
#     выдавать ошибки.


# Если Вы знаете с чем это может быть связано, то подскажите, пожалуйста!

import psycopg2  

conn = psycopg2.connect(database = 'Tips', user = 'postgres', password = '230611End')

# Функция, создающая структуру БД (таблицы)

def clients_base():
    with conn.cursor() as cur:
        # cur.execute("""
        # DROP TABLE clients;
        # """)
        cur.execute("""CREATE TABLE clients(
        id SERIAL PRIMARY KEY,
        name VARCHAR(80) UNIQUE NOT NULL,
        surname VARCHAR(80) UNIQUE NOT NULL,
        email VARCHAR(80) UNIQUE NOT NULL);
        """)
    conn.commit()        

def number_clients_base():
    with conn.cursor() as cur:
        # cur.execute("""
        # DROP TABLE clients_numbers;
        # """)    
        cur.execute("""CREATE TABLE clients_numbers(
        id SERIAL PRIMARY KEY,
        clients_id INTEGER NOT NULL REFERENCES clients(id),
        number INTEGER UNIQUE NOT NULL);
        """)
        conn.commit()

# Функция, позволяющая добавить нового клиента

def new_client():
    with conn.cursor() as cur:   
        cur.execute("""INSERT INTO clients(name, surname, email) 
        VALUES
        ('Сидор', 'Сидоров', 'sidorov@yandex.ru'),
        ('Иван', 'Иванов', 'ivanov@yandex.ru');
        """)
        cur.execute("""
        SELECT * FROM clients;
        """)
        conn.commit()
        print(cur.fetchall())
print(new_client())

# Функция, позволяющая добавить телефон для существующего клиента

def new_number():
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO clients_numbers(number)
        VALUES
        (89275486328),
        (89157469821);
        """)
        cur.execute("""
        SELECT * FROM clients;
        """)
        conn.commit()
        print(cur.fetchall()) 
print(new_number())    

# Функция, позволяющая изменить данные о клиенте

def update_client():
    with conn.cursor() as cur:
        cur.execute("""UPDATE clients 
            SET name = 'Василий', surname = 'Васильев', email = 'vasiliev@yandex.ru' 
            WHERE id = 2;
            """)
        conn.commit()
        print(cur.fetchall())
print(update_client())    

# Функция, позволяющая изменить номер телефона клиента

def update_number():
    with conn.cursor() as cur:
        cur.execute("""UPDATE clients_numbers 
            SET number = 89196542398,
            WHERE id = 2;
            """)
        conn.commit()
        print(cur.fetchall())
print(update_number())

# Функция, позволяющая удалить существующего клиента

def delete_client():
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM clients 
            WHERE id = 2;
            """)
        conn.commit()
        print(cur.fetchall())
print(delete_client())

# Функция, позволяющая удалить телефон для существующего клиента

def delete_number():
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM clients_numbers 
            WHERE id = 2;
            """)
        conn.commit()
        print(cur.fetchall())
print(delete_number())

# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

def get_clients_date():
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, surname, email, number FROM clients c
        JOIN clients_numbers cn ON c.id = cn.clients_id
        WHERE name = 'Иван';
        """)
        print(cur.fetchall())
print(get_clients_date())




conn.close()