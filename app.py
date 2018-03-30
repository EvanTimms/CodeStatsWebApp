from flask import Flask, render_template
from data import personalInfo
import pygal
#initalizing application as instance of flask class

app = Flask(__name__)
personal_info = personalInfo()

#build chart using pygal, will convert to query from database in future
def build_line_chart():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    line_chart = line_chart.render_data_uri()
    return line_chart

#adding routing decorator for intial bootup
@app.route('/')
def index():
    #builds charts
    chart = build_line_chart()
    #renders html web page
    return render_template('index.html', profile = personal_info, chart = chart)

#home route
@app.route('/index')
def home():
    chart = build_line_chart()
    return render_template('index.html', profile = personal_info, chart = chart)

#about route
@app.route('/about')
def about():
    return render_template('about.html')

#signin route
@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

#sign up route
@app.route('/signUp')
def singUp():
    return render_template('signUp.html')

if __name__ == "__main__":
    app.run(debug = True)