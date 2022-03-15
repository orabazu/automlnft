#!/home/ubuntu/anaconda3/bin/python
# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask
import subprocess
from functools import wraps
import os
from flask import send_file

def multiline(fn):
    @wraps(fn)
    def _fn(*args, **kwargs):
        return "<xmp>" + fn(*args, **kwargs) + "</xmp>"
    return _fn

proc = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print ("program output:", out)

app = Flask(__name__)

@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response
    

@app.route('/')
def hello_automlnft():
    cmd ="cat /home/ubuntu/automlnft/automl-models/for_iris_data/test_output"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

@app.route('/automl_iris_data_output')
def automl_iris_data():
    cmd ="cat /home/ubuntu/automlnft/automl-models/for_iris_data/iris_data_output"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

@app.route('/automl_restaurant_data_output')
def automl_restaurant_data():
    cmd ="cat /home/ubuntu/automlnft/automl-models/for_restaurant_data/restaurant_data_output"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

@app.route('/automl_report_iris_data')
def automl_report_iris_data():
    try:
        return send_file('/home/ubuntu/automlnft/automl-models/for_iris_data/Data_Analysis.pdf', attachment_filename='Data_Analysis.pdf')
    except Exception as e:
        return str(e)

@app.route('/automl_report_restaurant_data')
def automl_report_restaurant_data():
    try:
        return send_file('/home/ubuntu/automlnft/automl-models/for_restaurant_data/Data_Analysis.pdf', attachment_filename='Data_Analysis.pdf')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
