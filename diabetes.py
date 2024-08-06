# This code is based on the following tutorials:
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# https://machinelearningmastery.com/save-load-keras-deep-learning-models/
# and a bit from:
# https://keras.io/examples/structured_data/structured_data_classification_from_scratch/
# see also: https://github.com/keras-team/keras-io/blob/master/examples/structured_data/structured_data_classification_from_scratch.py

# dependencies:
# pip install tensorflow
# pip install numpy
# pip install h5py

# first neural network with keras tutorial
from numpy import loadtxt
from numpy import array
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense

# this is a public dataset (license CC0)
# see https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
# fields: pregnancies, glucose, BP, skin thickness (mm), insulin, BMI, DiabetesPedigreeFunction, Age, Outcome (diabetes y/n, 0 or 1) 
file_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataset = loadtxt(file_url, delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
# throws warning: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# make class predictions with the model
predictions = (model.predict(X) > 0.5).astype(int)
# summarize the first 5 cases
for i in range(5):
 print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

# demonstrate that we can make a prediction for a single patient
test = X[:1,:]
prediction = model.predict(test)
print(prediction)

# create a new numpy array to test
test2 = array([[6.,148., 72.,35.,0.,33.6,0.627,50.]])
prediction = model.predict(test2)
print(prediction)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    
# serialize weights to HDF5
model.save_weights("model.weights.h5")

# time passes...


## load json and create model
#json_file = open('model.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
## load weights into new model
#loaded_model.load_weights("model.weights.h5")
#print("Loaded model from disk")
#prediction = loaded_model.predict(test2)
#print(prediction)
