## https://lab-10-sgillihan-flask-hello-world.onrender.com/

from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello World from Stephanie Gillihan in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://sgillihan_lab_10_db_user:kTTPWao4DcXhVIneAbWvw9VVlWhYAdwL@dpg-d7a8jbp5pdvs73c31dkg-a/sgillihan_lab_10_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://sgillihan_lab_10_db_user:kTTPWao4DcXhVIneAbWvw9VVlWhYAdwL@dpg-d7a8jbp5pdvs73c31dkg-a/sgillihan_lab_10_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
