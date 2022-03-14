#!/usr/bin/python3
# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask
import subprocess

proc = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print ("program output:", out)

app = Flask(__name__)

@app.route('/')
def hello_automlnft():
    return 'Hello AutomMLNFT'

@app.route('/automl')
def automl():
    proc = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print ('out ', out)
    proc2 = subprocess.Popen(['/home/ubuntu/automlnft/automl-models/for_iris_data/automl.py'], stdout=subprocess.PIPE, shell=True)
    (out2, err) = proc2.communicate()
    #return 'AutoML Processing! ..... ' + out
    #res = out + out2
    res = out2
    return res

@app.route('/mlreport')
def automlreport():
    return 'AutoML PDF Report!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
