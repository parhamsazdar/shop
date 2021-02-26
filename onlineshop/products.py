from bson import ObjectId

from flask import Blueprint, request, render_template, current_app
from pymongo import MongoClient

from .manager import return_category

bp = Blueprint('products', __name__)


def cheep(name):
    database = current_app.config['DATABASE_NAME']
    client = MongoClient('localhost', 27017)
    db = client[database]
    y = list(db.inventory.aggregate(
        [{"$unwind": {"path": "$items"}}, {"$match": {"items.name_product": f"{name}", "items.quantity": {"$gt": 0}}},
         {"$sort": {"items.price": 1}},
         {"$limit": 1}]))

    return y[0]["items"]["name_product"], y[0]["name_inventory"]


def query_to_inventory(category=None):
    database = current_app.config['DATABASE_NAME']
    client = MongoClient('localhost', 27017)
    db = client[database]

    latest_products = list(db.inventory.aggregate([
        {"$unwind": {"path": "$items"}}, {"$sort": {"items.date_insert": -1, "items.price": 1}}]))
    data = {"گوشی": [], "لپ تاپ": [], "TV": []}
    lis_show = []
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

            if (category is None) and 'گوشی' in send_data['cat']:
                data['گوشی'].append(
                    [send_data['name_product'], f"{send_data['price']:,}", send_data['url_image'],
                     send_data['id_product']])
            elif (category is None) and 'لپ تاپ' in send_data['cat']:
                data['لپ تاپ'].append(
                    [send_data['name_product'], f"{send_data['price']:,}", send_data['url_image'],
                     send_data['id_product']])
            elif (category is None) and 'TV' in send_data['cat']:
                data['TV'].append(
                    [send_data['name_product'], f"{send_data['price']:,}", send_data['url_image'],
                     send_data['id_product']])




            elif category in send_data['cat'] and cheep_name == name and cheep_inv == var['name_inventory']:
                lis_show.append(
                    [send_data['name_product'], f"{send_data['price']:,}", send_data['url_image'],
                     send_data['id_product']])
    if lis_show:
        return lis_show
    else:
        return data


@bp.route('/')
def index():
    data = query_to_inventory()
    data = {'گوشی': data['گوشی'][0:6], 'لپ تاپ': data['لپ تاپ'][0:6], 'TV': data['TV'][0:6]}

    return render_template('index/index.html', data=data)


@bp.route('/category/?name=<category_name>', methods=['GET', 'POST'])
def category(category_name):
    lis_show = query_to_inventory(category=category_name)
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

    return render_template('index/new_products.html', lis_prod=lis_prod,
                           category_name=category_name, lis_show=lis_show)


@bp.route('/product/<product_id>')
def product(product_id):
    database = current_app.config['DATABASE_NAME']
    client = MongoClient('localhost', 27017)
    db = client[database]
    product = list(db.products.find({"_id": ObjectId(f'{product_id}')}))
    name_product = product[0]['name_product']
    inventory = list(db.inventory.aggregate(
        [{"$unwind": {"path": "$items"}},
         {"$match": {"items.name_product": f"{name_product}", "items.quantity": {"$gt": 0}}},
         {"$sort": {"items.price": 1}},
         {"$limit": 1}]))

    config_product = {"inventory_id": str(inventory[0]["_id"]), "price": f'{inventory[0]["items"]["price"]:,}',
                      "quantity": inventory[0]["items"]["quantity"],
                      "name_product": product[0]["name_product"], "category": product[0]["category"],
                      "url_image": product[0]["url_image"],

                      "description": product[0]["description"]}

    return render_template('index/product.html', config=config_product)


@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')


@bp.route('/cart/approve')
def cart_approve():
    print(request.args)
    return render_template('basket/checkout.html')
