from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, current_user


userpage = Blueprint('userpage', __name__)


@userpage.route('/', methods=['GET'])
@login_required
def user_panel():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template("userpage.html", user=current_user)
