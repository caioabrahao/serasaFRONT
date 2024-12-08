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



@app.route('/varpage')
def varpage():
    return render_template('bet_on_event.html')



@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/my_wallet')
def my_wallet():
    return render_template('my_wallet.html')

@app.route('/logout')
def logout():
    return render_template('frontpage.html')

@app.route('/search_events')
def search_events():
    return render_template('search_events.html')

@app.route('/add_new_event')
def add_new_event():
    return render_template('new_event.html')

@app.route('/add_funds')
def add_funds():
    return render_template('add_funds.html')

@app.route('/funds_history')
def funds_history():
    return render_template('funds_history.html')

@app.route('/add_funds_card')
def add_funds_card():
    return render_template('frontpage.html')

@app.route('/add_funds_pix')
def add_funds_pix():
    return render_template('frontpage.html')


app.run(debug=True)