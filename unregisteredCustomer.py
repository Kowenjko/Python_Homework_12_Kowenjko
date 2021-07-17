import psycopg2
from settings import *
from connection import Connection


class UnregisteredCuctomer(Connection):

    def register(self, data):
        if self._connectDb(self.login, self.password):
            table = 'customer'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def get_product_info(self):
        if self._connectDb(self.login, self.password):
            table = ('product_category',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    regCust = UnregisteredCuctomer()
    # orders = regCust.get_product_info()
    # print(orders)
    # ----------------------------------
    # data = [{
    #         'city_id': 2,
    #         'first_name': "Loman",
    #         'last_name': "Mipol"

    #         }]
    # put = regCust.register(data)
    # print(put)
