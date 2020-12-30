from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash


bp=Blueprint('products',__name__)



@bp.route('/')
def index():
    return render_template('index/index.html')
<<<<<<< HEAD



=======
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91




@bp.route('/category/?name=<category_name>',methods=['GET','POST'])
@bp.route('/category/')
def category():
    return render_template('template_masroori/new_products.html')




@bp.route('/product/<product_id>')
<<<<<<< HEAD
def product(product_id):
    return render_template('template_masroori/new_products.html')
=======
def product():
    pass
>>>>>>> 0ded1012376848a49fcb2b95b30ab163d4e5eb91



@bp.route('/cart')
def cart():
    return render_template('basket/basket.html')




@bp.route('/cart/approve')
def cart_approve():
    return render_template('basket/checkout.html')











