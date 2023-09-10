from flask_sqlalchemy import SQLAlchemy
from config.menu import load_menu

db = SQLAlchemy()


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    dish_amount = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text)  # Added description column
    image_url = db.Column(db.String(255))  # Added image URL column
    # ingredients = db.Column(db.Text)  # Added ingredients column
    # Added nutritional information column
    # nutritional_info = db.Column(db.Text)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, nullable=False)
    dish_name = db.Column(db.String(255), nullable=False)
    dish_amount = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    table_id = db.Column(db.Integer, nullable=False)
    order_datetime = db.Column(db.DateTime)  # Added order date/time column
    customer_name = db.Column(db.String(255))  # Added customer name column
    # Added special instructions column
    special_instructions = db.Column(db.Text)
    order_status = db.Column(db.String(50))  # Added order status column


def init_app(app):
    db.init_app(app)


def create_menu():
    menu_data = load_menu()

    for item in menu_data:
        new_item = FoodItem(
            dish_name=item['dish_name'],
            category=item['category'],
            dish_amount=item['dish_amount'],
            availability=item['availability'],
            description=item['description'],
            image_url=item['image_url']
        )
        db.session.add(new_item)
    db.session.commit()
