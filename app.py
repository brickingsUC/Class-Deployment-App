from flask import Flask, render_template, redirect, url_for, request, make_response
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = api_token(request.form['username'], request.form['password'])
        cookie = make_response(redirect(url_for('home')))
        cookie.set_cookie('Authorization', token['Authorization'])
        return cookie
    if 'Authorization' in request.cookies:
        redirect(url_for('home'))
    return render_template('login.html')

@app.route("/home")
def home():
    return request.cookies.get('Authorization')


def api_token(username, password):
    headers = {
        'Accept': 'application/json',            
        'Content-Type': 'application/json',
    }
    data = '{"username":"' + username + '","password":"' + password + '","tenant":"vsphere.local"}'
    url = 'https://sandbox02.cech.uc.edu/identity/api/tokens'
    response = requests.post(url=url, headers=headers, data=data, verify='certs/sandbox02-cech-uc-edu-chain.pem').json()
    auth = 'Bearer ' + response['id']
    headers.update({'Authorization': auth})

    return headers