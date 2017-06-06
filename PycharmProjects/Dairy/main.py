import functions

connection = functions.create_connection('database.db')
functions.create_table(connection)
commands = {}

while True:

    functions.main1(connection)



