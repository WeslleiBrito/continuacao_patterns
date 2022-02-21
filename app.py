from connection_factory import Connection_factory

cursor = Connection_factory().get_connection()

cursor.execute('SELECT * FROM cursor')

for linha in cursor:
    print(linha)

cursor.close()
