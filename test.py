import psycopg2 

password = '230611End'
# (Пароль от with psycopg2.connect удалил!!!)

def create_db(conn):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(80) UNIQUE NOT NULL,
                last_name VARCHAR(80) UNIQUE NOT NULL,
                email VARCHAR(80) UNIQUE NOT NULL);
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS clients_numbers(
                id SERIAL PRIMARY KEY,
                client_id INTEGER NOT NULL REFERENCES clients(id),
                phone BIGINT UNIQUE);
                """)
    conn.commit() 


def add_client(conn, first_name, last_name, email, phones=None):
    cur.execute("""
                INSERT INTO clients(first_name, last_name, email) 
                VALUES
                (%s, %s, %s);
                """, (first_name, last_name, email))
    conn.commit()


def add_phone(conn, client_id, phone):
    cur.execute("""
                INSERT INTO clients_numbers(client_id, phone)
                VALUES (%s, %s);
                """, (client_id, phone))
    conn.commit()



def change_client(conn, id, first_name=None, last_name=None, email=None):

    cur.execute("""
                UPDATE clients 
                SET first_name = coalesce(%s, first_name), last_name = coalesce(%s, last_name), email = coalesce(%s, email)               
                WHERE id = %s;
                """, (first_name, last_name, email, id))
    conn.commit()



def delete_phone(conn, client_id, phone):
    cur.execute("""
                DELETE FROM clients_numbers
                WHERE client_id = %s and phone = %s;
                """, (client_id, phone))
    conn.commit()


def delete_client(conn, id):
    client_id = id
    cur.execute("""
                DELETE FROM clients_numbers
                WHERE client_id = %s;
                """, (client_id,))
    cur.execute("""
                DELETE FROM clients
                WHERE id = %s;
                """, (id,))
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    # cur.execute("""
    #             SELECT first_name, last_name, email, phone FROM clients c
    #             JOIN clients_numbers cn ON c.id = cn.client_id
    #             WHERE first_name=%s, last_name=%s, email=%s, phone=%s;
    #             """, (first_name, last_name, email, phone))

    cur.execute("""
                SELECT first_name, last_name, email, phone FROM clients c
                JOIN clients_numbers cn ON c.id = cn.client_id
                WHERE (first_name is NULL OR first_name = first_name) AND (last_name is NULL OR last_name = last_name)
                AND (email is NULL OR email = first_name) AND (phone is NULL OR phone = phone);
                """, (first_name, last_name, email, phone))



    return print(cur.fetchone()) 
 



with psycopg2.connect(database = 'HomeWork', user = 'postgres', password = password) as conn:

    with conn.cursor() as cur:

        if __name__ == "__main__":

                # Функция, создающая структуру БД (таблицы)

            # create_db(conn)

                # Функция, позволяющая добавить нового клиента

            # add_client(conn, 'Сидор', 'Сидоров', 'sidorov@yandex.ru' )
            # add_client(conn, 'Иван', 'Иванов', 'ivanov@yandex.ru')

                # Функция, позволяющая добавить телефон для существующего клиента

            # add_phone(conn, 1, 89275486328)
            # add_phone(conn, 2, 89157469821) 
            # add_phone(conn, 2, 89048932568) 

                # Функция, позволяющая изменить данные о клиенте

            # change_client(conn, 2, 'Василий', 'Васильев', 'vasiliev@yandex.ru')    
            # change_client(conn, 2, 'Василий', email = 'vasiliev@yandex.ru')
                # Функция, позволяющая удалить существующего клиента

            # delete_client(conn, 1)

                # Функция, позволяющая удалить телефон для существующего клиента

            # delete_phone(conn, 2, 89157469821)

                # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

            find_client(conn, first_name='Иван', email='ivanov@yandex.ru')

            print('Success')

    cur.close() 
conn.close()