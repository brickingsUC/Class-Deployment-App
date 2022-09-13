from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from flask_cors import CORS
import requests
from vraApi.auth import api_token, api_token_valid
from vraApi.catalog import catalog_items


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def root():
    if 'Authorization' in request.cookies:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    return "<p>Hello</p>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if (('Authorization' in request.cookies) and (api_token_valid(request) == 204)):
        return redirect(url_for('home'))
    if request.method == 'POST':
        token = api_token(request.form['username'], request.form['password'])
        cookie = make_response(redirect(url_for('home')))
        cookie.set_cookie('Authorization', token['Authorization'], secure=True)
        return cookie
    return render_template('login.html')

@app.route("/home")
def home():
    if (('Authorization' not in request.cookies) or (api_token_valid(request)!= 204)):
        return redirect(url_for('login'))

    catalog_item_list = catalog_items(request.cookies.get('Authorization'))
    #return render_template('home.html', catalog_item_list=catalog_item_list['content'])
    return jsonify(catalog_item_list['content'])
@app.route("/deploy", methods=['GET', 'POST'])
def deploy():
    if (('Authorization' not in request.cookies) or (api_token_valid(request)!= 204)):
        return redirect(url_for('login'))

    if request.method == 'POST':
        uploaded_csv = request.files['uploaded-file']
        
        
        return render_template('deploy.html')
    return render_template('deploy.html')    



