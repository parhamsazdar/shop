from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash, jsonify
from pymongo import MongoClient

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.route('/product/list')
def prod_list():
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    prod_list = list(db.products.find())
    return jsonify(prod_list)


@bp.route('/product/<int:product_id>')
def prod_details(product_id):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    prod_details = list(db.products.find({"_id": product_id}))
    return jsonify(prod_details)


@bp.route('/product/add')
def prod_add():
    req=request.args.get('name')
    for i in request.args:
        print(i,':',request.args.get(i))
    return req


@bp.route('/product/edit')
def prod_edit():
    pass


@bp.route('/product/delete/<int:product_id>')
def prod_delete(product_id):
    client = MongoClient('localhost', 27017)
    db = client.online_shop
    db.products.delete_one({"_id": product_id})
    return jsonify(list(db.products.find()))
