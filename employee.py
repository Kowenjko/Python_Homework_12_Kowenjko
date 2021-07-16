import psycopg2
from settings import *
from connection import Connection


class Employee(Connection):

    def __init__(self, first_name, last_name, date_of_birth, city, chief, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.city = city
        self.chief = chief
        self.login = login
        self.password = password

    def edit_self_info(self):
        if self._connectDb(self.login, self.password):
            table = ('employee',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'

    def change_order_status(self):
        if self._connectDb(self.login, self.password):
            table = ('orders',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    employee = Employee('roma', 'romanich', '1953-02-03',
                        'London', 'Lok', 'admin', 'admin')
    # orders = employee.edit_self_info()
    # print(orders)
    # ------------------------------------
    orders = employee.change_order_status()
    print(orders)
