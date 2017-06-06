import sqlite3
import sys

table_name = 'diary'


# SQL_INSERT_TASK =


def create_connection(db_name):
    if db_name is None:
        db_name = ':memory:'
    connection = sqlite3.connect(db_name)
    return connection


def create_table(connection):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS diary (id INTEGER PRIMARY KEY AUTOINCREMENT, title, description, time, status)""")
    return


def create_task(connection, title, description, time):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO diary (title, description, time, status) VALUES (?, ?, ?, ?)", (
                title, description, time, 'not_performed'))
    return


def print_tasks(connection):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM diary""")
        task = cursor.fetchall()
        if task is None:
            print("\n")
            return
        else:
            print(task)
    return


def end_task(connection, task_id):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE diary SET status = '%s' WHERE id = '%d'" % (
            'performed', task_id))
    return


def start_task(connection, task_id):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE diary SET status = '%s' WHERE id = '%d'" % (
            'not_performed', task_id))
    return


def edit_task(connection, task_id, title, description, time):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE diary SET title = '%s', description = '%s', time = '%s' WHERE id = '%d'" % (
            title, description, time, task_id))
    return


# - обработчик действий


def show_menu():

    print('''
    1. Добавить задачу
    2. Вывести список задач
    3. Отредактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
    6. Выход''''\n')

    return


def main1(connection):

    commands = {
        '1': add_task,
        '2': show_tasks_list,
        '3': correct_task,
        '4': complete_task,
        '5': begin_task_again,
        '6': action_exit
    }

    while 1:

        show_menu()

        id_action = input('Выберите действие: ')
        action = commands.get(id_action)

        if action:
            action(connection)
        else:
            print('Неизвестная команда')


def add_task(connection):
    with connection as conn:
        task_name = str(input('Название задачи:'))
        description = str(input('Текст задачи:'))
        time = str(input('Дата:'))
        create_task(conn, task_name, description, time)


def show_tasks_list(connection):
    with connection as conn:
        print_tasks(conn)


def correct_task(connection):
    with connection as conn:
        print('Введите номер задачи:')
        task_id = int(input(''))
        print('Название задачи:')
        title = input('')
        print('Описание:')
        description = input('')
        print('Введите дату:')
        time = input()
        edit_task(conn, task_id, title, description, time)


def complete_task(connection):
    with connection as conn:
        print('Введите номер задачи:')
        task_id = int(input(''))
        end_task(conn, task_id)


def begin_task_again(connection):
    with connection as conn:
        print('Введите номер задачи:')
        task_id = int(input(''))
        start_task(conn, task_id)


def action_exit(connection):
    with connection:
        sys.exit(0)
