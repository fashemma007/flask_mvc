from flask import Flask,render_template
from config import DevConfig, ProdConfig

app = Flask(__name__)

## using our config class
# One point that may be unfamiliar to Flask users is the use of the
# phrase config.from_object rather than app.config['DEBUG']. We use from_object
#because in future, multiple configurations will be used, and manually changing #every variable when we need to switch between configurations is time consuming.

app.config.from_object(DevConfig)

@app.route('/')
def home():
    # return '<h1>Hello!</h1>'
    return render_template('base.html')

@app.route('/user',methods=['GET', 'POST'])
def user():
    return render_template('user.html')

if __name__ == '__main__':
    ## if app.py is run directly,
    # app.run(debug=True) ## run app and activate debugger
    app.run()