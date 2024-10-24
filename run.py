from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def frontpage():
    return render_template('frontpage.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/varpage')
# def varpage():
#     return render_template('new_event.html')

app.run()
# app.run(debug=True)