# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_automlnft():
    return 'Hello AutomMLNFT'

@app.route('/automl')
def automl():
    return 'AutoML Processing!'

@app.route('/mlreport')
def automlreport():
    return 'AutoML PDF Report!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
