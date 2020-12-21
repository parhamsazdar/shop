from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.online_shop
prod_list = list(db.products.find())
for i in prod_list:
    print(i)