from flask import Blueprint, jsonify, request
from db.init_db import FoodItem, db
from config.menu import update_menu

listmenu = Blueprint("list-menu", __name__)


@listmenu.route("/menu")
def get_menu():
    # Query all food items from the database
    menu_items = FoodItem.query.all()

    # Convert the menu items to a list of dictionaries
    menu_data = []
    for item in menu_items:
        item_dict = {}
        for column in item.__table__.columns:
            column_name = column.name
            column_value = getattr(item, column_name)
            item_dict[column_name] = column_value
        menu_data.append(item_dict)

    # Return the menu items as a JSON response
    return jsonify(menu=menu_data)


@listmenu.route("/menu/update", methods=["POST"])
def update_menu_item():
    # Get the JSON data from the POST request
    data = request.json

    # Extract the ID and fields to be updated from the JSON data
    item_id = data.get("id")
    new_availability = data.get("availability")
    new_price = data.get("dish_amount")

    # Query the FoodItem by ID
    menu_item = FoodItem.query.get(item_id)

    if menu_item:
        # Update the availability and/or price if provided in the request
        if new_availability is not None:
            menu_item.availability = new_availability
        if new_price is not None:
            menu_item.dish_amount = new_price

        # Commit the changes to the database
        db.session.commit()

        # update json file
        update_menu(menu_item)

        return jsonify(message="Item updated successfully"), 200
    else:
        return jsonify(message="Item not found"), 404
