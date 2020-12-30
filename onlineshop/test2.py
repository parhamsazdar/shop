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
from datetime import datetime

bp = Blueprint('test2', __name__, url_prefix="/test2")

@bp.route('/category/list')
def latest_products():
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    latest_products = list(db.inventory.find())
    # lis_products = db.products.find()
    lis = []
    lis_names = []
    for i in latest_products:
        lis.append((i["items"]))

    for item in lis:
        for j in item:
            lis_names.append((j["name_product"],j["price"]))
         
        # i["_id"] = str(i["_id"])
    return jsonify(lis_names)


@bp.route('/category/list_url',methods=('GET','POST'))
def products_url():
    param = request.form['name_product']

    client = MongoClient('localhost', 27017)
    db = client.online_shop
    products = list(db.products.find())
    for item in products:
        if item["name_product"] == param:
            return jsonify(item["url_image"])
    else:
        return jsonify('not found')

