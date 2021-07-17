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

    def edit_self_info(self, data, selector):
        role = 'employee'
        if self._connectDb(self.login, self.password, role):
            table = 'employee'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def change_order_status(self, data, selector):
        role = 'employee'
        if self._connectDb(self.login, self.password, role):
            table = ('orders',)
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    employee = Employee('roma', 'romanich', '1953-02-03',
                        'London', 'Lok', 'roman', '1234')
