from flask import Blueprint, render_template
from flask_login import current_user
from .models import Dish


menu =  Blueprint('menu', __name__)


@menu.route('/', methods=['GET'])
def menu_list():
    dish_list = Dish.query.all()
    return render_template('menu.html', dish_list=dish_list, user=current_user)
