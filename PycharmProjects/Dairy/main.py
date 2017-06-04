import functions

connection = functions.create_connection('database.sqlite')
functions.create_table(connection)
while True:
    print("1. Добавить задачу")
    print("2. Вывести список задач")
    print("3. Отредактировать задачу")
    print("4. Завершить задачу")
    print("5. Начать задачу сначала")
    print("6. Выход")

    a = int(input('Vyberite deystvie: '))

    if a == 1:
        task_name = str(input('Название задачи:'))
        description = str(input('Текст задачи:'))
        time = str(input('Дата:'))
        functions.create_task(connection, task_name, description, time)

    if a == 2:
        functions.print_tasks(connection)

    if a == 3:
        print('Введите номер задачи:')
        task_id = int(input(''))
        print('Название задачи:')
        title = input('')
        print('Описание:')
        description = input('')
        print('Введите дату:')
        time = input()
        functions.edit_task(connection, task_id, title, description, time)

    if a == 4:
        print('Введите номер задачи:')
        task_id = int(input(''))
        functions.end_task(connection, task_id)

    if a == 5:
        print('Введите номер задачи:')
        task_id = int(input(''))
        functions.start_task(connection, task_id)

    if a == 6:
        break
