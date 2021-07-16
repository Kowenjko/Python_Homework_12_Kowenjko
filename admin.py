import psycopg2
from settings import *
from connection import Connection


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self, data):
        table = 'login'
        if self._connectDb(self.login, self.password):
            if self._auditDb(table, list(data[0].values())[0]):
                result = self._postData(table, data)
                return result
            else:
                return 'A user with this login already exists'

        else:
            return 'Incorrect login or password'

    def add_product(self, data):
        if self._connectDb(self.login, self.password):
            table = 'product'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def add_pr_category(self, data):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def add_employee(self, data):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def delete_product(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'product'
            selector = f"product_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_pr_category(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            selector = f"category_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_employee(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_customer(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'customer'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_product(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'product'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_pr_category(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_employee(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def get_order_info(self, selector=''):
        if self._connectDb(self.login, self.password):
            table = ('orders',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    admin1 = Admin('admin', 'admin')
    # orders = admin1.get_order_info()
    # print(orders)
    # ----------------------------------
    # data = [{
    #         'category_name': "Coca"
    #         }]
    # put = admin1.add_pr_category(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'product_name': "Cola",
    #         'unit_price': 253,
    #         'country_id': 2,
    #         'product_catagery_id': 5
    #         }]
    # put = admin1.add_product(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'first_name': "Roms",
    #         'last_name': "Lom",
    #         'date_of_birds': "1953-04-10",
    #         'city_id': 1,
    #         'chief_id': 2
    #         }]
    # put = admin1.add_employee(data)
    # print(put)
    # ----------------------------------
    # data = [{
    #         'login': "Coca556",
    #         'password': "coca3"
    #         }]
    # put = admin1.register_self(data)
    # print(put)
    # # ----------------------------------
    # idf = admin1._getNextId('login')
    # print(idf)
    # ----------------------------------
    # data = {
    #     'product_name': "Water",
    #     'unit_price': 153,
    #     'country_id': 3,
    #     'product_catagery_id': 1
    # }
    # edit = admin1.edit_product(data, "product_name = 'Cola'")
    # print(edit)
    # ----------------------------------
    # data = {
    #     'first_name': "lopes",
    #     'last_name': "Lodm",
    #     'date_of_birds': "2003-04-10",
    #     'city_id': 2,
    #     'chief_id': 1
    # }
    # edit = admin1.edit_employee(data, "first_name = 'Roms'")
    # print(edit)
    # ----------------------------------
    # data = {
    #     'category_name': "Water"
    # }
    # edit = admin1.edit_pr_category(data, "category_name = 'Coca'")
    # print(edit)
    # ----------------------------------
    # log = admin1._connectDb('admin', 'admin')
    # print(log)
    # ----------------------------------
    # dele = admin1.delete_pr_category('Water')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_product('Cola')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_employee('Roms')
    # print(dele)
    # ----------------------------------
    # dele = admin1.delete_customer('Rola')
    # print(dele)
