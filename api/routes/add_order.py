from flask import Blueprint, request, jsonify
from db.init_db import db, Order
from datetime import datetime

add_order = Blueprint("add-order", __name__)


@add_order.route("/add-order", methods=["POST"])
def add_orders():
    try:
        # Get the JSON data from the POST request
        order_data = request.json

        # Create a list to store the Order objects
        orders_to_add = []

        # Iterate through the array of order data
        for item in order_data:
            table_id = item.get("table_id")
            dish_name = item.get("dish_name")
            dish_amount = item.get("dish_amount")
            quantity = item.get("quantity")
            customer_name = item.get("customer_name")
            special_instructions = item.get("special_instructions")
            order_status = item.get("order_status")

            # Calculate the total amount
            total_amount = dish_amount * quantity

            # Create a new Order object and add it to the list
            new_order = Order(
                table_id=table_id,
                dish_name=dish_name,
                dish_amount=dish_amount,
                quantity=quantity,
                total_amount=total_amount,
                order_datetime=datetime.now(),
                customer_name=customer_name,
                special_instructions=special_instructions,
                order_status=order_status
            )

            orders_to_add.append(new_order)

        # Add all orders to the session and commit the changes to the database
        db.session.add_all(orders_to_add)
        db.session.commit()

        return jsonify(message="Orders added successfully"), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
