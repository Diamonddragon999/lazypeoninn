from flask import Blueprint, render_template, flash, request, send_file
from flask_login import current_user
from .models import Media


media =  Blueprint('media', __name__)


@media.route('/list', methods=['GET'])
def media_list():
    media_list = Media.query.all()
    return render_template('media.html', media_list=media_list, user=current_user)


@media.route('/get', methods=['GET'])
def media_get():
    if 'file' not in request.args:
        flash('File not found!', 'error')
        media_list = Media.query.all()
        return render_template("media.html", media_list=media_list, user=current_user)
    else:
        file_name = request.args.get('file')
        return send_file(file_name)

