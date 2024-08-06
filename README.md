# Python_ML_web_app_demo
This repo provides the materials for a simple demo of a Python web app that incorporates a machine-learning-based clinical prediction model. Note that this is a technical demo; it is not intended to be used to make clinical decisions.

Step 1: Build the model and export it to files. I used the Pima Indians Diabetes data set, following (more or less) the instructions here:
https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

The code for building the model and exporting it to a file is found in [diabetes.py](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/diabetes.py).

Step 2: Set up a hosting service. I'm using PythonAnywhere: https://www.pythonanywhere.com/

Step 3: Set up services on the hosting platform. I followed this tutorial: https://www.pythonanywhere.com/user/drace/task_helpers/start/3-web_app/
followed by this one: https://blog.pythonanywhere.com/121/ .
I then created a new database called ehr
```
create database ehr;
use drace$ehr;
```

Step 4: Set up the database schema and some test data. The SQL can be found in [database.sql](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/database.sql).

Step 5: Upload the model. This is done via the Files page on pythonanywhere. Note that pythonanywhere uses specific python versions (specified on setup), which come with specific versions of packages. You may need to upgrade the version of the package on pythonanywhere (if you have enough disk space) or downgrade your version of one or more packages and rebuild the model in order to export it in a format that avoids version compatability issues.
Upgrading may be possible using:
`pip install --user --upgrade packagename==2.2.0`
(specify the version number after the ==)
or
`pip install --upgrade packagename==2.2.0`
Downgrading may be possible using:
`pip install packagename==1.1.0`

Alternatively, you may have to find and install using the .whl file:
`pip install packagename.whl`
You may need to specify the full path, e.g.: `pip install C:/directory/packagname.whl`

Also note that installing packages takes a lot of CPU, which is very limited in the free pythonanywhere service. This is a good reason to build your model on your own machine, and export it.

The files for the saved, trained model are found in [model.json](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/model.json) and [model.weights.h5](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/model.weights.h5).


Step 6: Set up template and python files to:
1. load patients from the database and allow a patient to be selected by clicking
2. allow the user to enter a value by hand (in this case it replaces a value in the database, but it could also be used to add a value that wasn't already in the data)
3. make a prediction for the current patient, using the model

Note: This *should* work using a flask_app file like [flask_app_my_model.py](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/flask_app_my_model.py) and the prediction model file [my_model.py](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/my_model.py). However, this does not work on pythonanywhere because of this error: https://www.pythonanywhere.com/forums/topic/27530/ .
However, it does work if tensorflow is run from bash (the command line) rather than directly from the webapp.

Thus the flow is:
1. The webapp gets the parameters from the database and/or the form fields, and puts them into a bash shell command.
2. Using package os, we call the python script my_shell_model.py with the parameters as arguments.
3. The my_shell_model.py script writes its result to a file.
4. The flask app checks that the script ran successfully (exit code 0) and then reads the result from the file.

Although calling Python from a shell called from Python is a little obtuse, in a way, it's a good illustration. This same method could be used to get a result from *any* program that can write to a file. Thus it could also be used to get a result from an R model, for example.

The example that's running on pythonanywhere is using these files:
* /home/drace/mysite/[flask_app.py](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/flask_app.py)
* /home/drace/mysite/[templates/main_page.html](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/templates/main_page.html)
* /home/drace/[my_shell_model.py](https://github.com/ace-dvm/Python_ML_web_app_demo/blob/main/my_shell_model.py)
* and the two model files from step 5, in the /home/drace/mysite/ directory

Note: There are some extra "print" statements to help with debugging. These are visible in the log files. Also: Yes, I know this page is ugly. The objective is to show how the back end works, not to make a nice front end.
