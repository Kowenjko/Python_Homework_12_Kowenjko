import psycopg2
from settings import *
from connection import Connection


class UnregisteredCuctomer(Connection):

    def register(self, data):
        table = 'customer'
        result = self._postData(table, data)
        return result

    def get_product_info(self):
        table = ('product_category',)
        fields = ('*',)
        selector = ''
        result = self._getData(table, fields, selector)
        return result


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
