# A very simple example Flask app demonstrating how a machine learning model can be used to make a tool for predicting risk for an individual patient.
# This is purely a demo, and is not in any way intended to be used for medical advice.

import os
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="drace",
    password="MariaDB_is_better",
    hostname="drace.mysql.pythonanywhere-services.com",
    databasename="drace$ehr",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Patient(db.Model):

    __tablename__ = "patient"

    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(100))
    num_pregnancies = db.Column(db.Integer())
    glucose = db.Column(db.Integer())
    blood_pressure_dias = db.Column(db.Integer())
    skin_thickness = db.Column(db.Integer())
    insulin = db.Column(db.Integer())
    BMI = db.Column(db.Float())
    diab_pedigree = db.Column(db.Float())
    age = db.Column(db.Integer())

patients = Patient.query.all()

current_patient = patients[0]

userbp = None

def get_prediction(current_patient,userbp):
    bp = current_patient.blood_pressure_dias
    if userbp:
        bp = int(userbp)

    systemcall = "python my_shell_model.py " + str(current_patient.num_pregnancies) + " " + str(current_patient.glucose) + " " + str(bp) + " " + str(current_patient.skin_thickness) + " " + str(current_patient.insulin) + " " + str(current_patient.BMI) + " " + str(current_patient.diab_pedigree) + " " + str(current_patient.age)
    print(systemcall)
    result = os.system(systemcall)

    if result == 0:
        file = open("/home/drace/mysite/prediction_result","r")
        prediction = file.read()
        file.close()
    else:
        prediction = ""

    return prediction

prediction = get_prediction(current_patient,userbp)

@app.route("/", methods=["GET", "POST"])
def index():
    global userbp
    global prediction
    if request.method == "GET":
        return render_template("main_page.html", patients=patients, userbp=userbp, current_patient=current_patient, prediction=prediction)

    userbp = request.form['userbp']
    prediction = get_prediction(current_patient,userbp)
    return redirect(url_for('index'))


@app.route('/my-link/<patient_id>')
def my_link(patient_id=0):
    global current_patient
    global prediction
    global userbp
    userbp = None
    id = int(patient_id)-1
    current_patient = patients[id]
    prediction = get_prediction(current_patient,userbp)
    return redirect(url_for('index'))
