from flask import Flask, render_template

#initalizing application as instance of flask class

app = Flask(__name__)

#adding routing decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/signUp')
def singUp():
    return render_template('signUp.html')

if __name__ == "__main__":
    app.run(debug = True)