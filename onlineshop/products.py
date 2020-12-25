from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash


bp=Blueprint('products',__name__)



@bp.route('/')
def index():
    return render_template('index/index.html')







@bp.route('/category/؟name=<category_name>')
def category():
    pass




@bp.route('/product/<product_id>')
def product():

    pass

@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')


@bp.route('/cart/approve')
def cart_approve():
    return render_template('basket/checkout.html')
#










