import os
from flask import Flask
from db.init_db import db, init_app, create_menu
from api.routes.home_page import homepage
from api.routes.list_menu import listmenu
from api.routes.get_table import get_table
from api.routes.add_order import add_order
from api.routes.get_orders import get_orders

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    base_url = "/api/v1"
    app = Flask(__name__)

    # initialize sql-alchemy configs
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, '../config/food_menu.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # sqlite db initialize and creation
    with app.app_context():
        init_app(app)
        db.drop_all()
        db.create_all()
        create_menu()

    app.register_blueprint(homepage)
    app.register_blueprint(listmenu, url_prefix=base_url)
    app.register_blueprint(get_table, url_prefix=base_url)
    app.register_blueprint(add_order, url_prefix=base_url)
    app.register_blueprint(get_orders, url_prefix=base_url)

    return app
