from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
from math import *

expression = ''
li = []
cur = 0

@app.route("/", methods=["GET", "POST"])
def index():
	global expression
	global n
	global cur
	if request.method == "POST":
		num = request.form["bt"]
		if (num == 'CE'):
			expression = ''
		elif (num == 'C'): 
			expression = expression[:-1]
		elif (num == '='):
			li.append(expression)
			print(li)
			expression = str(eval(expression))
			return render_template("index.html",all_users=expression)
		elif (num == '<'):
			expression = li[-1+cur]
			cur = cur-1
			if (cur > len(li) or cur < -len(li)):
				error = 'error'
				return render_template("index.html",all_users=error)
			else:
				return render_template("index.html",all_users=expression)
		elif (num == '>'):
			expression = li[cur+1]
			cur+=1
			if (cur > len(li) or cur < -len(li)):
				error = 'error'
				return render_template("index.html",all_users=error)
			else:
				return render_template("index.html",all_users=expression)
		else:
			expression = expression + str(num)

		return render_template("index.html",all_users=expression)
	return render_template("index.html")
'''
@app.route("/Hello")
def hello():
	return render_template("index.html", all_users=eval(expression))
'''
