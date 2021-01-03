from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash


bp=Blueprint('products',__name__)



@bp.route('/')
def index():
    return render_template('index/index.html')





@bp.route('/category/؟name=<category_name>')
def category():
    return render_template('template_masroori/new_products.html')




@bp.route('/product/')
def product():
<<<<<<< HEAD
    pass
=======
    return render_template('index/inventory.html')



>>>>>>> 507abe23b5614082b0284863b387328d301cb070



@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')




@bp.route('/cart/approve')
def cart_approve():
    print(request.args)
    return render_template('basket/checkout.html')











