from flask import Blueprint,url_for,session,request,render_template,redirect,g,flash,current_app
import pymongo


# def create_database():
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     store_1 = myclient["store_1"]
#     store_2 = myclient["store_2"]
#     store_3 = myclient["store_3"]
#


def get_db():
    if "db" not in g:
        g.db= pymongo.MongoClient("mongodb://localhost:27017/")

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()



def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
