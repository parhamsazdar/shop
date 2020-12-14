from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash


bp=Blueprint('products',__name__)



@bp.route('/')
def index():

    return render_template('index.html')











