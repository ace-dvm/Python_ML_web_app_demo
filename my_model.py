from numpy import array
from tensorflow.keras.models import model_from_json
from datetime import datetime

# load json and create model
json_file = open('/home/drace/mysite/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights
loaded_model.load_weights("/home/drace/mysite/model.weights.h5")


def get_prediction(current_patient,userbp):
    bp = current_patient.blood_pressure_dias
    if userbp:
        bp = int(userbp)

    params = array([[current_patient.num_pregnancies,current_patient.glucose,bp,current_patient.skin_thickness,current_patient.insulin,current_patient.BMI,current_patient.diab_pedigree,current_patient.age]])
    print("Made param array")
    prediction = prediction_model(params)
    print("returned model result")
    return prediction

def prediction_model(params):
    print("entered prediction_model")
    prediction = 0
    prediction = loaded_model.predict(params)
    print("got model result")
    return prediction
