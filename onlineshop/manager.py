import io

from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash
import hashlib
import json

bp = Blueprint('manager', __name__, url_prefix='/manager')


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


def register_manager(user, password):
    password = str(password)
    obj = hashlib.sha256()
    obj.update(password.encode())
    li = [user, obj.hexdigest()]
    with open(r'onlineshop/manager_info.json', 'r') as f:
        f = json.load(f)
    if li in f:

        return True
    else:
        global error
        error = 'WRONG MANAGER'


def logout():
    if session['manager'] is None:
        session.pop('manager', None)
    return redirect(url_for('products.index'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if session.get('manager') is None:
        return render_template('manager/login.html')
    else:
        return redirect(url_for('manager.manage_panel'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':

        if register_manager(request.form['username'], request.form['password']):
            session['manager'] = request.form['username']

            return redirect(url_for('manager.manage_panel'))
        else:
            flash("نام کاربری یا رمز عبور اشتباه است")
            return render_template('manager/login.html')


@bp.route('/logout')
def logout():
    session.pop('manager', None)
    return redirect(url_for('products.index'))


@bp.route('/panel')
def manage_panel():
    return render_template('manager/base_manager.html')


@bp.route('/products')
def manage_products():
    return render_template('manager/products.html',category=return_category(r'onlineshop/category.json'))


@bp.route('/inventory')
def manage_inventory():
    return render_template('manager/inventory.html')


@bp.route('/quantity')
def manage_quantity():
    return render_template('manager/quantity.html')


@bp.route('/orders')
def manage_orders():
    return render_template('manager/orders.html')
