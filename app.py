from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/verse')
def verse():
    return render_template('verse.html')

if __name__ == '__main__':
    app.run(debug=True)