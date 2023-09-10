from flask import Blueprint, request, jsonify
from db.init_db import Order

get_orders = Blueprint("get-orders", __name__)


@get_orders.route("/get-orders", methods=["POST"])
def retrieve_orders_by_table_id():
    try:
        # Get the JSON data from the POST request
        request_data = request.json
        # Check if the request data contains the 'table_id' key
        if 'table_id' not in request_data:
            return jsonify(error="Table ID is required in the request data"), 400

        table_id = request_data['table_id']

        # Query all orders with the specified table_id
        orders = Order.query.filter_by(table_id=table_id).all()

        # Convert the orders to a list of dictionaries
        orders_data = []
        for order in orders:
            order_dict = {
                "id": order.id,
                "table_id": order.table_id,
                "dish_name": order.dish_name,
                "dish_amount": order.dish_amount,
                "quantity": order.quantity,
                "total_amount": order.total_amount,
                "order_datetime": order.order_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                "customer_name": order.customer_name,
                "special_instructions": order.special_instructions,
                "order_status": order.order_status
            }
            orders_data.append(order_dict)

        return jsonify(orders=orders_data), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
