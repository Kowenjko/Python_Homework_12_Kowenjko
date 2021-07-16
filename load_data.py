
import psycopg2
from psycopg2 import Error
from settings import *
from faker import Faker
from random import randint

arr_chees = 'Cheddar', 'Queso ', 'Cotija', 'Pecornio', 'Romano', 'Graviera', 'Brunost', 'Edam', 'Raclette', 'Tomme', 'Swiss', 'Langres', 'Fontina ', 'Stilton', 'Taleggio', 'Havarti', 'Jarlsberg', 'Valdeon', 'Pepper Jack', 'Ossau-Iraty', 'Rubens', 'Esrom'
arr_fruits = 'Mango', 'Grape ', 'Nectarine', 'Strawberry', 'Cherry', 'Pear', 'Orange', 'Watermelon', 'Banana', 'Jackfruit', 'Papaya', 'Kiwi', 'Pineapple ', 'Lime', 'Lemon', 'Apricot', 'Grapefruit', 'Melon', 'Coconut', 'Avocado', 'Rubens', 'Plum'
arr_meat = 'Pork', 'Beef ', 'Lamb', 'Mutton', 'Chicken', 'Turkey', 'Venison', 'Duck', 'Wild ', 'Boar', 'Bison', 'Goose', 'Rabbit ', 'Pheasant', 'Duck', 'Chicken', 'Mutton', 'Lamb', 'Duck', 'Pork', 'Beef', 'Goose'
arr_fishs = 'Goby ', 'Anabas ', 'Eel', 'Catfish', 'Anchovy', 'Snapper', 'Grouper', 'Bluegill', 'Scad ', 'Red drum', 'Garfish', 'Zander', 'Goldfish ', 'Guppy', 'Nile tilapia', 'Ayu', 'Blue tang', 'Swordfish', 'White bass', 'Neon tetra', 'Red drum', 'Atlantic mackerel'
arr_drinks = 'Beer ', 'Cider ', 'Cocktails', 'Hard soda', 'Wine', 'Barley', 'Mixed drinks', 'Coffee', 'Hot chocolate ', 'Lemon tea', 'Soft drinks', 'Milk', 'Water ', 'Juice drinks', 'Green tea', 'Beer cocktail', 'Coconut water', 'Orange juice', 'Apple juice', 'Almond milk', 'White lady', 'Sidecar'
fake = Faker()

try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT,
                                  database="shop_db")

    cursor = connection.cursor()
    # add product db-----------------------------------------------------
    j = 0
    for i in range(0, len(arr_fruits)):
        insert_query = f""" INSERT INTO  product (ID, product_name, unit_price, country_id, product_catagery_id)
                                    VALUES
                                    ({i+j+7},'{(arr_chees[i])}',{randint(49, 500) },{randint(1, 5) }, 1),
                                    ({i+j+8},'{(arr_meat[i])}',{randint(49, 500) },{randint(1, 5) }, 3),
                                    ({i+j+9},'{(arr_fruits[i])}',{randint(49, 500) },{randint(1, 5) }, 2),
                                    ({i+j+10},'{(arr_drinks[i])}',{randint(49, 500) },{randint(1, 5) }, 5),
                                    ({i+j+11},'{(arr_fishs[i])}',{randint(49, 500) },{randint(1, 5) }, 4)

                    """
        j += 5
        cursor.execute(insert_query)
        connection.commit()
    # add city---------------------------------------------------------------

    for i in range(4, 54):
        insert_city = f""" INSERT INTO  city (ID, city_name, country_id)
                                   VALUES
                                    ({i},'{fake.city()}',{randint(1, 5) })                                 
                    """
        cursor.execute(insert_city)
        connection.commit()

# -------------------------------------------------
except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
