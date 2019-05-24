from flask import Flask, request, flash, url_for, redirect, render_template
from datetime import datetime
import pyodbc
from app import db

server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

app = Flask(__name__)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)

castit_cursor = cnxn.cursor()

class Part_Input(db.Model):
    ts = db.Column(db.TIMESTAMP() = NOW())
    partno = db.Column(db.String(10))
    lot = db.Column(db.int())
    hanger = db.Column(db.int())

def __init__(self, ts, partno, lot, hanger):
    self.ts = ts
    self.partno = partno
    self.lot = lot
    self.hanger = hanger

db.create_all()

@app.route('/')
def show_all():
    return render_template('show_all.html', par.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['PN'] or not request.form['LOT'] or not request.form['HANGER']:
            flash('Please enter all the fields', 'error')
        else:
            part = PART_CAST(NOW(), request.form['PN'], request.form['LOT'], request.form['HANGER'])

        db.session.add(part)
        db.session.commit()
        flash('Record was successfully added')
        return redirect url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
