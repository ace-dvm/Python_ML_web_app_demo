import sys
from numpy import array
from tensorflow.keras.models import model_from_json
from datetime import datetime

# static params for testing
test1 = array([[6.,148., 72.,35.,0.,33.6,0.627,50.]])
test2 = array([[2,106,56,27,165,29.0,0.426,22]])
test3 = array([[2,174,88,37,120,44.5,0.646,24,1]])
test4 = array([[4,95,60,32,0,35.4,0.284,28]])
test5 = array([[0,126,86,27,120,27.4,0.515,21]])


# load json and create model
json_file = open('/home/drace/mysite/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
print(datetime.now())
print("loaded model")
# load weights
loaded_model.load_weights("/home/drace/mysite/model.weights.h5")
print(datetime.now())
print("loaded weights")

def get_prediction(num_pregnancies,glucose,bp,skin_thickness,insulin,BMI,diab_pedigree,age):
    params = array([[float(num_pregnancies),float(glucose),float(bp),float(skin_thickness),float(insulin),float(BMI),float(diab_pedigree),float(age)]])
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

predict = get_prediction(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
file = open("/home/drace/mysite/prediction_result","w")
file.write(str(predict))
file.close()