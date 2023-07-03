from flask import Flask, render_template
import requests
import os

httpd_service = os.getenv('HTTPD-HOST',None)

app = Flask(__name__)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print("hier")
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return "You clicked the Action 1 button"
        elif request.form.get('action2') == 'VALUE2':
            return requests.get(f"http://{httpd_service}").text
            #return requests.get("http://httpd-service").text
            #return redirect("http://httpd-app:8080", code=302)
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('index.html')#, form=form)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")