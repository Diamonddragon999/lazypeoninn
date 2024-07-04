from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from .models import Review, User
import sqlite3
import uuid
from . import db
from . import DB_NAME


review =  Blueprint('review', __name__)


@review.route('/list', methods=['GET'])
def review_list():

    review_list = Review.query.all()

    shortened_reviews = []

    for review in review_list:
        shortened_reviews.append({
            'review_title': review.review_title,
            'review_text': review.review_text[0:300] + '...',
            'review_code': review.review_code,
        })

    return render_template('review.html', review_list=shortened_reviews, user=current_user)

@review.route('/read', methods=['GET'])
def read_review():
    if 'code' not in request.args:
        return render_template('read.html', user=current_user, review_data=None)
    
    review_code = request.args.get('code')

    conn = sqlite3.connect('./instance/' + DB_NAME)
    cur = conn.cursor()
    query = f"""SELECT author, review_title, review_text FROM review r JOIN user u ON r.author=u.id where r.review_code='{review_code}';"""
    cur.execute(query)
    review = cur.fetchall()

    if review:
        author = review[0][0]
        title = review[0][1]
        text = review[0][2]

        author = User.query.get(author)

        if not author:
            return render_template('read.html', user=current_user, review=None)
        
        review = {
            'review_author': author.name,
            'review_title': title,
            'review_text': text
        }

        return render_template('read.html', user=current_user, review=review)
    
    else:
        return render_template('read.html', user=current_user, review=None)

@review.route('/write', methods=['POST'])
def write_review():
    review_author = current_user.id
    review_title = request.form['review_title']
    review_text = request.form['review_text']

    review_to_add = Review(author=review_author, review_title=review_title, review_text=review_text, review_code=uuid.uuid4().hex)

    db.session.add(review_to_add)
    db.session.commit()

    flash('Review successfully posted!', 'success')

    return redirect(url_for('review.review_list'))