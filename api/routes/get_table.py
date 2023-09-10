from flask import Blueprint, jsonify
from db.init_db import Order
import random

get_table = Blueprint("get-table", __name__)


@get_table.route("/get-table", methods=["GET"])
def generate_unique_table_id():
    while True:
        # Generate a random table ID between 1 and 99
        table_id = random.randint(1, 99)

        # Check if the generated table ID already exists in the Order table
        existing_order = Order.query.filter_by(table_id=table_id).first()

        # If the table ID does not exist, return it
        if not existing_order:
            return jsonify(table_id=table_id)
