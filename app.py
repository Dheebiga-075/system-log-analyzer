from flask import Flask, render_template, request
import os

app = Flask(_name_)

LOG_FILE = "logs/sample.log"

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    if request.method == 'POST':
        keyword = request.form['keyword']

        with open(LOG_FILE, 'r') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    errors.append(line.strip())

    return render_template('index.html', errors=errors)

if _name_ == '_main_':
    app.run(debug=True)