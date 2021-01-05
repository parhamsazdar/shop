import io
import json

from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash, jsonify
from pymongo import MongoClient

from .manager import return_category

bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    send_data = {}
    data = {"تلفن همراه": [], "لپ تاپ": [], "تلویزیون": []}
    latest_products = list(db.inventory.aggregate([
        {"$unwind": {"path": "$items"}}, {"$sort": {"items.price": -1, "items.date_insert": 1}}]))
    for var in latest_products:
        name = send_data['name_product'] = var["items"]["name_product"]
        # send_data['date_insert'] = var["items"]["date_insert"]
        send_data['price'] = var["items"]["price"]
        # send_data['id_product'] = var["_id"]
        cli = list(db.products.find({"name_product": name}))
        print(cli)
        send_data['url_image'] = cli[0]['url_image']
        send_data['id_product'] = cli[0]['_id']
        send_data['cat'] = cli[0]['category']

        if 'گوشی' in send_data['cat']:
            data['تلفن همراه'].append(
                [send_data['url_image'], send_data['name_product'], send_data['price'], send_data['id_product']])
        elif 'لپ تاپ' in send_data['cat']:
            data['لپ تاپ'].append(
                [send_data['url_image'], send_data['name_product'], send_data['price'], send_data['id_product']])
        elif 'tv' in send_data['cat']:
            data['تلویزیون'].append(
                [send_data['url_image'], send_data['name_product'], send_data['price'], send_data['id_product']])

    print(data)

    return render_template('/template_masroori/mainpage.html', data=data)


@bp.route('/category/?name=<category_name>', methods=['GET', 'POST'])
def category(category_name):

    # values = request.form['name2']
    category_name = category_name
    lis = return_category(r'onlineshop/category.json')
    lis_goshi = []
    lis_tv = []
    lis_lop = []
    print("||||||||||||||||||||||||||||",category_name)
    for item in lis:
        if 'کالای دیجیتال/گوشی' in item:
            lis_goshi.append(item.split('/')[2])
    for item in lis:
        if 'کالای دیجیتال/TV' in item:
            lis_tv.append(item.split('/')[2])
    for item in lis:
        if 'کالای دیجیتال/لپ تاپ' in item:
            lis_lop.append(item.split('/')[2])
    lis_prod = {"تلفن همراه": lis_goshi, "تلویزیون": lis_tv, "لپ تاپ": lis_lop}
    if request.method == 'POST':
        values = json.dumps(request.form['name2'])
        print("=======+++++++++values+++++++>>>.", values)
        return render_template('template_masroori/new_products.html', values=values, lis_prod=lis_prod,
                               category_name=category_name)
    return render_template('template_masroori/new_products.html', lis_prod=lis_prod,
                           category_name=category_name)


@bp.route('/product/<product_id>')
def product(product_id):
    return render_template('template_masroori/new_products.html')


@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')


@bp.route('/cart/approve')
def cart_approve():
    return render_template('basket/checkout.html')
#
