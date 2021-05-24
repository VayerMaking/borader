from flask import Flask
from flask import render_template, request, flash, redirect, url_for, session, make_response, jsonify
import time
import os
from datetime import datetime

app = Flask(__name__)

web_ui_settings = {"setting1" : 1, "setting2" : 2}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(web_ui_settings)
        return render_template('index.html', web_ui_settings=web_ui_settings)
    elif request.method == 'POST':
        data = request.form
        new_settings = {"setting1" : data['setting1'], "setting2" : data['setting2']}
        web_ui_settings.update(new_settings)
        return redirect(url_for('index'))


def server_run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
