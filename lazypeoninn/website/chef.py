from flask import Blueprint, render_template, request, render_template_string
from flask_login import current_user
from .models import Chef
import re


chef =  Blueprint('chef', __name__)

sanitized_regex = [
    '.*socket.*',
	'.*connect.*',
	'.*spawn.*',
	'.*[1-9].*'
]


@chef.route('/list', methods=['GET'])
def chef_list():
	chef_list = Chef.query.all()
	return render_template('chef.html', chef_list=chef_list, user=current_user)


@chef.route('/info', methods=['GET'])
def chef_info():
	if 'code' not in request.args:
		return render_template('error.html', user=current_user)
   
	code = request.args.get('code')

	chef = Chef.query.filter_by(employee_code=code).first()

	if chef:
		chef_info = {
			'name': chef.name,
			'description': chef.description,
			'avatar': chef.avatar
		}

		return render_template('info.html', chef_info=chef_info, user=current_user)
	else:
		for regex in sanitized_regex:
			p = re.compile(regex)

			code = code.replace('\\x', '')

			if p.match(code):
				verified_regex = ', '.join(sanitized_regex)
				return '<h2>Malicious activity detected. One of the following expressions was used: ' + verified_regex +  '. You are not meant to open any shells on target.</h2> <a class="nav-link font-weight-bold" href="/chef/list">Go Back</a>'

		template = '<h2>Chef with code %s not found!</h2> <a class="nav-link font-weight-bold" href="/">Go Back</a>' % code
		return render_template_string(template)
