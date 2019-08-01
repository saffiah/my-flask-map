#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	print 'hi.....inside Python'
	data = request.get_json(force=True)

	result = ''
	print "data is ", data
	# for item in data:
	# 	# loop over every row
	# 	make = str(item['make'])
	# 	if(make == 'Porsche'):
	# 		result += make + '---That is fancy car!\n'
	# 	else:
	# 		result +=make + '---Ok, average car.\n'
	result = json.dumps(data);
	return result

if __name__ == '__main__':
	# run!
	app.run(debug=True)