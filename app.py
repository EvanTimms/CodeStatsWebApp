from flask import Flask, render_template

#initalizing application as instance of flask class

app = Flask(__name__)

#adding routing decorator
@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)