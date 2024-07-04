from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from .models import User
from werkzeug.security import generate_password_hash
import uuid
from . import db

register = Blueprint('register', __name__)


@register.route('/', methods=['GET', 'POST'])
def register_page():

    if request.method == 'POST':
        email = request.form.get('email')
        
        existing_email = User.query.filter_by(email=email).first()

        if existing_email:
            flash('An user with this e-mail already exists!', 'error')
        else:
            password = request.form.get('password')
            name = request.form.get('name')

            user_to_add = User(email=email, password=generate_password_hash(password), name=name, user_code=uuid.uuid4().hex)
            
            db.session.add(user_to_add)
            db.session.commit()

            flash('User succesfully registered!', 'success')

    return render_template("register.html", user=current_user)
