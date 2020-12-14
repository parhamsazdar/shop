

from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash
import hashlib
import json

bp=Blueprint('manager',__name__,url_prefix='/manager')



def register_manager(user,password):
    password = str(password)
    obj = hashlib.sha256()
    obj.update(password.encode())
    li=[user,obj.hexdigest()]
    with open(r'onlineshop/manager_info.json', 'r') as f:
        f = json.load(f)
    if li in f:

        return True
    else:
        global error
        error='WRONG MANAGER'


def logout():
    if session['manager'] is None:
        session.pop('manager',None)
    return redirect(url_for('products.index'))




@bp.route('/login',methods=('GET','POST'))
def login():
    return render_template('login.html')



@bp.route('/register',methods=('GET','POST'))
def register():

    error='parham'
    if request.method=='POST':
        if register_manager(request.form['username'],request.form['password']):
            session['manager'] = request.form['username']

            return redirect(url_for('manager.manage_panel'))
        else:
            return render_template('login.html',error=error)




@bp.route('/logout')
def logout():
    print(session['manager'])
    if session['manager'] is None:
        session.pop('manager',None)
    return redirect(url_for('products.index'))





@bp.route('/panel')
def manage_panel():
    return render_template('manager.html')


@bp.route('/products')
def manage_products():
    pass



@bp.route('/store')
def manage_store():
    pass






