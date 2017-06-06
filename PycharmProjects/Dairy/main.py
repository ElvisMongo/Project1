import functions

connection = functions.create_connection('database.db')
functions.create_table(connection)

while True:

    functions.main1(connection)



