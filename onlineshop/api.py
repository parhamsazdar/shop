import json
from bson import ObjectId
from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash, jsonify
from pymongo import MongoClient
import io
from json import load

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.route('/product/list')
def prod_list():
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    prod_list = list(db.products.find())
    for i in prod_list:
        i["_id"] = str(i["_id"])

    return jsonify(prod_list)


@bp.route('/product/<product_id>')
def prod_details(product_id):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    prod_details = list(db.products.find({"_id": product_id}))
    return jsonify(prod_details)


@bp.route('/product/add', methods=('GET', 'POST'))
def prod_add():
    if request.method == "POST":
        client = MongoClient('localhost', 27017)
        db = client.online_shop
        prob_add = {"name_product": request.form.get('product_name'), "description": request.form.get('description'),
                    "category": request.form.get('category'), "url_image": r"/static/images/surface.jpg"}
        res = db.products.insert_one(prob_add)

        db = list(db.products.find({"_id": res.inserted_id}))
        for i in db:
            i["_id"] = str(i["_id"])

        return jsonify(db)


@bp.route('/product/edit',methods=('GET', 'POST'))
def prod_edit():
    if request.method == "POST":
        client = MongoClient('localhost', 27017)
        db = client.online_shop

        db.products.update({"_id":ObjectId(request.form.get('_id'))},{"$set":{"name_product": request.form.get('product_name'), "description": request.form.get('description'),
                    "category": request.form.get('category'), "url_image": r"/static/images/surface.jpg"}})
        res=list(db.products.find({"_id":ObjectId(request.form.get('_id'))}))
        print(res)
        for i in res:
            i["_id"] = str(i["_id"])


        return jsonify(res)


@bp.route('/product/delete/<product_id>')
def prod_delete(product_id):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    db.products.delete_one({"_id": ObjectId(product_id)})
    res = list(db.products.find())
    for i in res:
        i["_id"] = str(i["_id"])
    return jsonify(res)


@bp.route('/product/json_category')
def prod_json_category():
    with io.open(r'onlineshop/category.json', encoding='utf-8') as f:
        f = load(f)
        return jsonify(f)
