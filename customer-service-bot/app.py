from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['text']
    result = foo(data)
    return json.dumps(result)


def foo(input: str):
    # Your implementation here
    pass


if __name__ == '__main__':
    app.run(debug=True)
