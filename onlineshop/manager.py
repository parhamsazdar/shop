from flask import Blueprint, url_for, session, request, render_template, redirect, g, flash
import hashlib
import json

bp = Blueprint('manager', __name__, url_prefix='/manager')


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
    return render_template('login.html')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    error = 'parham'
    if request.method == 'POST':
        if register_manager(request.form['username'], request.form['password']):
            session['manager'] = request.form['username']

            return redirect(url_for('manager.manage_panel'))
        else:
            return render_template('login.html', error=error)


@bp.route('/logout')
def logout():
    print(session['manager'])
    if session['manager'] is None:
        session.pop('manager', None)
    return redirect(url_for('products.index'))


@bp.route('/panel')
def manage_panel():
    return render_template('template_masroori/base_manager.html')


@bp.route('/products')
def manage_products():
    return render_template('template_masroori/products.html')


@bp.route('/inventory')
def manage_inventory():
    return render_template('template_masroori/inventory.html')


@bp.route('/quantity')
def manage_quantity():
    return render_template('template_masroori/quantity.html')


@bp.route('/orders')
def manage_orders():
    return render_template('template_masroori/orders.html')
