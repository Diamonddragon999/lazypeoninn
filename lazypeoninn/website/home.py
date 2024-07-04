from flask import Blueprint, request, render_template
from flask_login import current_user
import os
from . import DB_NAME
from . import db
import sqlite3

home =  Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def home_page():
    return render_template('home.html', user=current_user)

@home.route('/api/cache-key', methods=['POST'])
def cache_key():
    api_key = request.headers.get('Api-Key')
    file_name = request.headers.get('File-Name') + "-api-key.txt"
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, file_name)

    if api_key and file_name:
        for fname in os.listdir(directory):
            if fname.endswith("-api-key.txt"):
                return {"message": "Another API key file already exists"}, 200
        if os.path.exists(file_path):
            return {"message": "File already exists"}, 200
        try:
            with open(file_path, 'w') as file:
                file.write(api_key)
            return {"message": "API key saved successfully"}, 200
        except Exception as e:
            return {"message": str(e)}, 500
    return {"message": "Api-Key and File-Name headers are required"}, 400


@home.route('/api/place/flag-1', methods=['POST'])
def place_flag_1():
    api_key = request.headers.get('Api-Key')
    directory = os.path.dirname(os.path.abspath(__file__))
    flag = request.data.decode('utf-8')

    if not api_key:
        return {"message": "Api-Key header is required"}, 400

    # Find the existing -api-key.txt file
    api_key_file = None
    for fname in os.listdir(directory):
        if fname.endswith("-api-key.txt"):
            api_key_file = os.path.join(directory, fname)
            break

    if not api_key_file:
        return {"message": "No API key file found"}, 400

    # Check if the Api-Key matches the one in the file
    with open(api_key_file, 'r') as file:
        stored_api_key = file.read().strip()

    if api_key != stored_api_key:
        return {"message": "Invalid API key"}, 403

    try:
        with open(os.path.join('website/static/files/', 'flag.txt'), 'w') as file:
            file.write(flag)
        return {"message": "Flag 1 placed successfully"}, 200
    except Exception as e:
        return {"message": str(e)}, 500

@home.route('/api/get/flag-1', methods=['GET'])
def get_flag_1():
    api_key = request.headers.get('Api-Key')
    directory = os.path.dirname(os.path.abspath(__file__))

    if not api_key:
        return {"message": "Api-Key header is required"}, 400

    # Find the existing -api-key.txt file
    api_key_file = None
    for fname in os.listdir(directory):
        if fname.endswith("-api-key.txt"):
            api_key_file = os.path.join(directory, fname)
            break

    if not api_key_file:
        return {"message": "No API key file found"}, 400

    # Check if the Api-Key matches the one in the file
    with open(api_key_file, 'r') as file:
        stored_api_key = file.read().strip()

    if api_key != stored_api_key:
        return {"message": "Invalid API key"}, 403

    try:
        with open(os.path.join('website/static/files/', 'flag.txt'), 'r') as file:
            flag = file.read()
        return {"flag": flag}, 200
    except Exception as e:
        return {"message": str(e)}, 500

@home.route('/api/place/flag-2', methods=['POST'])
def place_flag_2():
    api_key = request.headers.get('Api-Key')
    directory = os.path.dirname(os.path.abspath(__file__))
    flag = request.data.decode('utf-8')

    if not api_key:
        return {"message": "Api-Key header is required"}, 400

    # Find the existing -api-key.txt file
    api_key_file = None
    for fname in os.listdir(directory):
        if fname.endswith("-api-key.txt"):
            api_key_file = os.path.join(directory, fname)
            break

    if not api_key_file:
        return {"message": "No API key file found"}, 400

    # Check if the Api-Key matches the one in the file
    with open(api_key_file, 'r') as file:
        stored_api_key = file.read().strip()

    if api_key != stored_api_key:
        return {"message": "Invalid API key"}, 403

    # Update the flag in the database
    try:
        conn = sqlite3.connect('./instance/' + DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE dish SET ingredients = ? WHERE id = ?", (flag, 7))
        conn.commit()
        conn.close()
        return {"message": "Flag 2 placed successfully"}, 200
    except Exception as e:
        return {"message": str(e)}, 500
    
@home.route('/api/get/flag-2', methods=['GET'])
def get_flag_2():
    api_key = request.headers.get('Api-Key')
    directory = os.path.dirname(os.path.abspath(__file__))

    if not api_key:
        return {"message": "Api-Key header is required"}, 400

    # Find the existing -api-key.txt file
    api_key_file = None
    for fname in os.listdir(directory):
        if fname.endswith("-api-key.txt"):
            api_key_file = os.path.join(directory, fname)
            break

    if not api_key_file:
        return {"message": "No API key file found"}, 400

    # Check if the Api-Key matches the one in the file
    with open(api_key_file, 'r') as file:
        stored_api_key = file.read().strip()

    if api_key != stored_api_key:
        return {"message": "Invalid API key"}, 403

    # Retrieve the flag from the database
    try:
        conn = sqlite3.connect('./instance/' + DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT ingredients FROM dish WHERE id = ?", (7,))
        flag = cursor.fetchone()
        conn.close()
        if flag:
            return {"flag": flag[0]}, 200
        else:
            return {"message": "Flag not found"}, 404
    except Exception as e:
        return {"message": str(e)}, 500