from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/scan')
def scanner():
     return render_template("scan.html")

@app.route('/scanlogin', methods=['GET'])
def scanlogin():
    datav = {
        "client_id":"0000000044169C92",
        "redirect_uri":"http://localhost:8000/scanlogin",
        "client_secret":"GaC9yzLcDLu7gPBlQ6hFZo6kUjFLjEB7",
        "code":request.args.get('code', ''),
        "grant_type":"authorization_code"
        }
    values = requests.post("https://login.live.com/oauth20_token.srf", data=datav)
    return str(requests.get("https://api.onedrive.com/v1.0/drive",params={"access_token":values.json().get("access_token")}).json())

        


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)