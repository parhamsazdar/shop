from bson import ObjectId
from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash
from pymongo import MongoClient

bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    return render_template('index/index.html')


@bp.route('/category/؟name=<category_name>')
def category():
    return render_template('template_masroori/new_products.html')


@bp.route('/product/<product_id>')
def product(product_id):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    product = list(db.products.find({"_id": ObjectId(f'{product_id}')}))
    name_product = product[0]['name_product']
    inventory = list(db.inventory.aggregate(
        [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": f"{name_product}"}},
         {"$sort": {"items.price": 1}},
         {"$limit": 1}]))

    config_product = {"inventory_id": str(inventory[0]["_id"]), "price": inventory[0]["items"]["price"],
                      "quantity": inventory[0]["items"]["quantity"],
                      "name_product": product[0]["name_product"], "category": product[0]["category"],
                      "url_image": product[0]["url_image"],
                      "description": product[0]["descrption"]}

    return render_template('index/product.html', config=config_product)


@bp.route('/cart')
def cart():

    return render_template('basket/basket.html')


@bp.route('/cart/approve')
def cart_approve():
    return render_template('basket/checkout.html')
