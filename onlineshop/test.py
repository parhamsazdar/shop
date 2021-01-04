from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.online_shop

res = list(db.products.find({"_id": ObjectId('5ff2cc92c95917dde264b54b')}))
name_product = res[0]['name_product']
# print(list(res))
#
#
# print(name_product)
#
# res_2=db.inventory.aggregate({"$unwi"})
y = list(db.inventory.aggregate(
    [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": f"{name_product}"}},
     {"$sort": {"items.price": 1}},
     {"$limit": 1}]))



# a = {"inventory_id": y[0]["_id"], "price": y[0]["items"]["price"], "quantity": y[0]["items"]["quantity"],
#      "name_product": res[0]["name_product"], "category": res[0]["category"], "url_image": res[0]["url_image"],
#      "description": res[0]["descrption"]}

# print(y)
