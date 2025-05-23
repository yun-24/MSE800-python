from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/great/<name>')
def great(name):
    return f"{name}, have a nice day."

@app.route('/<name>/<int:hour>')
def learn(name, hour):
    return f"{name} learns at {hour}."

if __name__ == '__main__':
    app.run(debug=True)
