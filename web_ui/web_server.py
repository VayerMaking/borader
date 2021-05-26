from flask import Flask
from flask import render_template, request, flash, redirect, url_for, session, make_response, jsonify
import time
import os
from datetime import datetime
import psycopg2
from sqlalchemy import create_engine
import config

engine_str = 'postgresql://' + config.db_usr + ':' + config.db_pass + '@localhost/borader'
engine = create_engine(engine_str)

app = Flask(__name__)

def get_setting():
    with engine.begin() as cn:
        sql = """SELECT * FROM web_ui_settings"""
        data = cn.execute(sql).fetchall()
    return data

def update_db(wus):
    with engine.begin() as cn:
        a,b,c = wus['setting1'], wus['setting2'], wus['setting3']
        sql = """UPDATE web_ui_settings  SET (setting1, setting2, setting3) = (%s, %s, %s);"""
        #UPDATE films SET kind = 'Dramatic' WHERE kind = 'Drama';
        val = (a, b, c)
        cn.execute(sql, val)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        #print(web_ui_settings)
        return render_template('index.html', web_ui_settings=list(get_setting()[0]))
    elif request.method == 'POST':
        data = request.form

        new_settings = {"setting1" : int(data['setting1']), "setting2" : int(data['setting2']), "setting3" : int(data['setting3'])}
        update_db(new_settings)
        #web_ui_settings.update(new_settings)
        return redirect(url_for('index'))


def server_run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
