import json
import os

from bson import ObjectId
from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash, jsonify
from pymongo import MongoClient
import io
from json import load
import xlrd
from werkzeug.utils import secure_filename
import openpyxl
from pathlib import Path

bp = Blueprint('api', __name__, url_prefix="/api")


def return_category(filename):
    li = []
    with io.open(filename, encoding='utf-8') as f:
        f = json.load(f)
        category = f[0]
        for i in range(len(category['subcategories'])):
            cat2 = category['name']
            cat2 += r'/' + category['subcategories'][i]['name']
            for j in range(len(category['subcategories'][0]['subcategoreis'])):
                cat3 = cat2
                cat3 += r'/' + category['subcategories'][i]['subcategoreis'][j]['name']
                li.append(cat3)
                cat3 = cat2
    return li


def check_validation_excel(path):
    category = []
    xlsx_file = Path(path)
    wb_obj = openpyxl.load_workbook(xlsx_file)
    sheet = wb_obj.active
    for row in sheet.iter_rows(max_row=sheet.max_row):
        if row[-2].value not in return_category(r'onlineshop/category.json'):
            raise Exception('your category is wrong')
        else:
            category.append({
                'name_product': row[-1].value,
                'category': row[-2].value,
                'descrption': row[-3].value,
                'url_image': row[-4].value
            })
    return category


def opencon(func):
    client = MongoClient('localhost', 27017)
    db = client.online_shop

    def wrapper(*args, **kwargs):
        func(db)

    return wrapper


@bp.route('/product/list')
def prod_list():
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    prod_list = list(db.products.find())
    for i in prod_list:
        i["_id"] = str(i["_id"])
    return jsonify(prod_list)


@bp.route('/product/<product_id>')
def prod_details(product_id, db):
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


@bp.route('/product/edit', methods=('GET', 'POST'))
def prod_edit():
    if request.method == "POST":
        client = MongoClient('localhost', 27017)
        db = client.online_shop
        db.products.update({"_id": ObjectId(request.form.get('_id'))}, {
            "$set": {"name_product": request.form.get('product_name'), "description": request.form.get('description'),
                     "category": request.form.get('category'), "url_image": r"/static/images/surface.jpg"}})
        res = list(db.products.find({"_id": ObjectId(request.form.get('_id'))}))
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


@bp.route('/product/upload', methods=('GET', 'POST'))
def upload_file_category():
    if request.method == 'POST':
        f = request.files['file']
        f.save(r'onlineshop/uploads/' + secure_filename(f.filename))
        try:
            category = check_validation_excel(fr'onlineshop/uploads/{secure_filename(f.filename)}')
            client = MongoClient('localhost', 27017)
            db = client.online_shop
            for i in category:
                res = db.products.insert_one(i)
                i['_id'] = str(res.inserted_id)
            return jsonify(category)
        except Exception as ex:
            return jsonify([{'error': f'{ex}'}])
        finally:
            os.remove(fr'onlineshop/uploads/{secure_filename(f.filename)}')


@bp.route('/product/json_category')
def prod_json_category():
    with io.open(r'onlineshop/category.json', encoding='utf-8') as f:
        f = load(f)
        return jsonify(f)
