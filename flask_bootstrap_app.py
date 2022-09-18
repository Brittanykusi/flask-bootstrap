from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('p1_homepage.html')

@app.route('/patient_landing')
def landing():
    return render_template('p3_patient_landing_page.html')

@app.route('/login2')
def login():
    return render_template('p4_login2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)