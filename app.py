from flask import Flask, render_template
from jobs import JOBS

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(debug=True)