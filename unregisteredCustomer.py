import psycopg2
from settings import *
from connection import Connection


class UnregisteredCuctomer(Connection):

    def register(self, data, data_2):
        table = 'login'
        table_2 = 'customer'
        if self._auditDb(table, list(data[0].values())[0]):
            result = self._postData(table, data)
            result_2 = self._postData(table_2, data_2)
            return result+result_2
        else:
            return 'A user with this login already exists'

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
    #         'login': "Loman",
    #         'password': "Mipol",
    #         'role': "customer"
    #         }]
    # data_2 = [{
    #     'city_id': 2,
    #     'first_name': "Loman",
    #     'last_name': "Mipol"
    # }]
    # put = regCust.register(data, data_2)
    # print(put)
