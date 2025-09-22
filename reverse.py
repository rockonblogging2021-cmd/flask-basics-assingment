from flask import Flask

app = Flask(__name__)

@app.route('/reverse/<string:text>')
def reverse_string(text):
    return text[::-1]

if __name__ == '__main__':
    app.run(debug=True)
