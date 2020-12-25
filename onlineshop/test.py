from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
# db = client.online_shop
# prod_list = list(db.products.find())
# for i in prod_list:
#     print(i)


def opencon(func):
    # client = MongoClient('localhost', 27017)
    # db = client.online_shop
    def wrapper(*args,**kwargs):
        client = MongoClient('localhost', 27017)
        db = client.online_shop
        func(db)

    return wrapper


@opencon
def ali(db):
    prod_list = list(db.products.find())
    for i in prod_list:
        print(i)

ali()