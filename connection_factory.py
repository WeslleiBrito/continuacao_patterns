import MySQLdb


class Connection_factory(object):

    def get_connection(self):
        connection = MySQLdb.connect(
            host='localhost',
            user='root',
            password='',
            db='alura')

        return connection


cursor = Connection_factory().get_connection()

cursor.execute('SELECT * FROM cursor')

for linha in cursor:
    print(linha)

connection.close()
