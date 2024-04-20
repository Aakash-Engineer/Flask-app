from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'jj'

if __name__ == '__main__':
    app.run(debug=True)