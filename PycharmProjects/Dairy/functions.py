import sqlite3

table_name = 'diary'


# SQL_INSERT_TASK =


def create_connection(db_name):
    if db_name is None:
        db_name = ':memory:'
    connection = sqlite3.connect(db_name)
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS diary (id INT PRIMARY KEY, title, description, time, status)""")
    return


def create_task(connection, title, description, time):
    task_id = get_id(connection)

    cursor = connection.cursor()
    cursor.execute("INSERT INTO diary (id, title, description, time, status) VALUES ('%d', '%s', '%s','%s','%s')" % (
        task_id, title, description, time, 'not_performed'))
    connection.commit()
    return


def print_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM diary""")
    while True:
        task = cursor.fetchone()
        if task is None:
            print("\n")
            return
        else:
            print(task)


def get_id(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM diary""")
    count = 1
    while True:
        tasks = cursor.fetchone()# - берет значение в последней строчке первого столбца. Т. е. значение id.
        if tasks is None:
            return count
        count += 1


def end_task(connection, task_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE diary SET status = '%s' WHERE id = '%d'" % (
        'performed', task_id))
    connection.commit()
    return


def start_task(connection, task_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE diary SET status = '%s' WHERE id = '%d'" % (
        'not_performed', task_id))
    connection.commit()
    return


def edit_task(connection, task_id, title, description, time):
    cursor = connection.cursor()
    cursor.execute("UPDATE diary SET title = '%s', description = '%s', time = '%s' WHERE id = '%d'" % (
        title, description, time, task_id))
    connection.commit()
    return
