import psycopg2
from settings import *


class Connection():

    @classmethod
    def _openDB(cls):
        connection = psycopg2.connect(user=USER, password=PASSWORD,
                                      host=HOST, port=PORT,
                                      database='shop_db')
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def _closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def _auditDb(self, table, login):
        connection, cursor = self._openDB()
        audit_query = f"""SELECT * FROM {table} where login='{login}';"""
        cursor.execute(audit_query)
        connection.commit()
        result = cursor.fetchall()
        self._closeDB(connection, cursor)
        if result:
            return False
        else:
            return True

    def _connectDb(self, login, password):
        connection, cursor = self._openDB()
        table = 'login'
        connect_query = f"""SELECT * FROM {table} where login='{login}' and "password"='{password}';"""
        cursor.execute(connect_query)
        connection.commit()
        result = cursor.fetchall()
        self._closeDB(connection, cursor)
        if result:
            return True
        else:
            return False

    def _getData(self, table: tuple, fields: tuple, selector=''):
        connection, cursor = self._openDB()
        select_query = f"""SELECT {','.join(fields)} FROM {','.join(table)} {selector};"""
        cursor.execute(select_query)
        connection.commit()
        result = cursor.fetchall()
        self._closeDB(connection, cursor)
        return result

    def _postData(self, table, data: list):
        connection, cursor = self._openDB()
        next_id = self._getNextId(table)
        # print(next_id)
        fields = list(data[0].keys())
        fields.append('id')
        values = ''
        for row in data:
            value = f"""({','.join(map(lambda item: f"'{item}'" ,row.values()))}, {next_id}),"""
            next_id += 1
            values += value
        insert_query = f"""INSERT INTO {table} ({','.join(fields)}) VALUES {values[:-1]};"""
        cursor.execute(insert_query)
        connection.commit()
        self._closeDB(connection, cursor)
        return 'Insert done!'

    def _updateData(self, table, data: dict, selector: str):
        connection, cursor = self._openDB()
        set_items = ''
        for key in data:
            set_items += f"{key} = '{data[key]}',"

        update_query = f"""UPDATE {table} SET {set_items[:-1]} WHERE {selector}"""
        cursor.execute(update_query)
        connection.commit()
        self._closeDB(connection, cursor)
        return 'Update done!'

    def _deleteData(self, table, selector=''):
        connection, cursor = self._openDB()
        delete_query = f"""DELETE FROM {table} WHERE {selector};"""
        cursor.execute(delete_query)
        connection.commit()
        self._closeDB(connection, cursor)
        return 'Item was deleted!'

    def _getNextId(self, table):
        table = (table,)
        fields = ('id',)
        result = sorted(self._getData(table, fields))[-1][0]+1
        return result
