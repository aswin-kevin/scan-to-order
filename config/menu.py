import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))
json_path = os.path.join(basedir, 'food_menu.json')


def load_menu():
    menu_list = json.load(open(json_path))
    return menu_list["menu"]


def update_menu(menu_item):
    updated_item = {column.name: getattr(
        menu_item, column.name) for column in menu_item.__table__.columns}

    old_menu = json.load(open(json_path))
    for item in old_menu['menu']:
        if item['dish_name'] == updated_item['dish_name']:
            # Update the specified fields (availability or price)
            if 'availability' in updated_item:
                item['availability'] = updated_item['availability']
            if 'dish_amount' in updated_item:
                item['dish_amount'] = updated_item['dish_amount']

    out = open(json_path, "w")
    json.dump(old_menu, out, indent=4)
    out.close()
