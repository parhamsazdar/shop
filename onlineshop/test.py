import functools

from bson import ObjectId
from flask import url_for
from persiantools.jdatetime import JalaliDateTime
from pymongo import MongoClient
from werkzeug.utils import redirect

# client = MongoClient('localhost', 27017)
# db = client.online_shop
#
# res = list(db.products.find({"_id": ObjectId('5ff2cc92c95917dde264b54b')}))
# name_product = res[0]['name_product']
# # print(list(res))
# #
# #
# # print(name_product)
# #
# # res_2=db.inventory.aggregate({"$unwi"})
# y = list(db.inventory.aggregate(
#     [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": f"{name_product}"}},
#      {"$sort": {"items.price": 1}},
#      {"$limit": 1}]))
#
#
#
# # a = {"inventory_id": y[0]["_id"], "price": y[0]["items"]["price"], "quantity": y[0]["items"]["quantity"],
# #      "name_product": res[0]["name_product"], "category": res[0]["category"], "url_image": res[0]["url_image"],
# #      "description": res[0]["descrption"]}
#
# # print(y)
#
# def login_required(view):
#     """View decorator that redirects anonymous users to the login page."""
#
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         client = MongoClient('localhost', 27017)
#         db = client.online_shop
#
#         return view(**kwargs)
#
#     return wrapped_view
# from persiantools.jdatetime import JalaliDate, JalaliDateTime
# time=r'1399-10-23'
# # print(JalaliDateTime.now().to_gregorian())
# print(JalaliDateTime.fromisoformat(time).to_gregorian())
