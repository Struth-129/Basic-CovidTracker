from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get("https://disease.sh/v2/countries/India")
    data = data.json()
    return render_template('index.html',data = data)

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

if __name__ == "__main__":
    app.run(debug=True) 