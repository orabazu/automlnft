#!/home/ubuntu/anaconda3/bin/python
# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask
import subprocess
from functools import wraps
import os

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
    #cmd="date"
    # /home/ubuntu/automlnft/automl-models/for_iris_data/test_output
    cmd ="cat /home/ubuntu/automlnft/automl-models/for_iris_data/test_output"
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    #return 'Hello AutomMLNFT'
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

@app.route('/mlreport')
def automlreport():
    #proc3 = subprocess.Popen(["cat", "/home/ubuntu/automlnft/automl-models/for_iris_data/test_output"], stdout=subprocess.PIPE, shell=True)
    cmd ="cat /home/ubuntu/automlnft/automl-models/for_iris_data/test_output"
    #proc3 = subprocess.Popen(["cat", "/home/ubuntu/automlnft/automl-models/for_iris_data/test_output"], stdout=subprocess.PIPE, shell=True)
    proc3 = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out3 = proc3.communicate()[0].decode("utf-8")
    #return 'AutoML PDF Report!'
    response3 = app.response_class(response3=out3, status=200, mimetype='application/txt')
    return response3

if __name__ == '__main__':
    app.run(host='0.0.0.0')
