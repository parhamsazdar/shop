from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash, jsonify
from pymongo import MongoClient

from .manager import return_category

bp = Blueprint('products', __name__)


def cheep(name):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    y = list(db.inventory.aggregate(
        [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": f"{name}"}},
         {"$sort": {"items.price": 1}},
         {"$limit": 1}]))

    return y[0]["items"]["name_product"], y[0]["name_inventory"]


@bp.route('/')
def index():
    client = MongoClient('localhost', 27017)
    db = client.online_shop

    latest_products = list(db.inventory.aggregate([
        {"$unwind": {"path": "$items"}}, {"$sort": {"items.price": 1, "items.date_insert": -1}}]))
    data = {"گوشی": [], "لپ تاپ": [], "TV": []}
    for var in latest_products:
        send_data = {}
        send_data['price'] = var["items"]["price"]
        name = send_data['name_product'] = var["items"]["name_product"]
        cheep_name, cheep_inv = cheep(name)
        if name == cheep_name and var["name_inventory"] == cheep_inv:

            cli = list(db.products.find({"name_product": name}))
            send_data['url_image'] = cli[0]['url_image']
            send_data['id_product'] = cli[0]['_id']
            send_data['cat'] = cli[0]['category']

            if 'گوشی' in send_data['cat']:
                data['گوشی'].append(
                    [send_data['name_product'], send_data['price'], send_data['url_image'], send_data['id_product']])
            elif 'لپ تاپ' in send_data['cat']:
                data['لپ تاپ'].append(
                    [send_data['name_product'], send_data['price'], send_data['url_image'], send_data['id_product']])
            elif 'TV' in send_data['cat']:
                data['TV'].append(
                    [send_data['name_product'], send_data['price'], send_data['url_image'], send_data['id_product']])

    data = {'گوشی': data['گوشی'][0:6], 'لپ تاپ': data['لپ تاپ'][0:6], 'TV': data['TV'][0:6]}
    return render_template('/template_masroori/mainpage.html', data=data)


@bp.route('/category/?name=<category_name>', methods=['GET', 'POST'])
def category(category_name):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    latest_products = list(db.inventory.aggregate([
        {"$unwind": {"path": "$items"}}, {"$sort": {"items.price": 1, "items.date_insert": -1}}]))
    lis_show = []
    for var in latest_products:
        send_data = {}
        name = send_data['name_product'] = var["items"]["name_product"]
        send_data['price'] = var["items"]["price"]

        cli = list(db.products.find({"name_product": name}))
        send_data['url_image'] = cli[0]['url_image']
        send_data['id_product'] = cli[0]['_id']
        send_data['cat'] = cli[0]['category']
        if category_name in send_data['cat']:
            lis_show.append(
                [send_data['name_product'], send_data['price'], send_data['url_image'], send_data['id_product']])

    category_name = category_name
    lis = return_category(r'onlineshop/category.json')
    lis_goshi = []
    lis_tv = []
    lis_lop = []

    for item in lis:
        if 'کالای دیجیتال/گوشی' in item:
            lis_goshi.append(item.split('/')[2])
        elif 'کالای دیجیتال/TV' in item:
            lis_tv.append(item.split('/')[2])
        elif 'کالای دیجیتال/لپ تاپ' in item:
            lis_lop.append(item.split('/')[2])
    lis_prod = {"گوشی": lis_goshi, "TV": lis_tv, "لپ تاپ": lis_lop}

    return render_template('template_masroori/new_products.html', lis_prod=lis_prod,
                           category_name=category_name, lis_show=lis_show)


@bp.route('/product/<product_id>')
def product(product_id):
    return render_template('template_masroori/new_products.html')


@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')


@bp.route('/cart/approve')
def cart_approve():
    return render_template('basket/checkout.html')
