from flask import Flask, render_template, request, redirect, url_for, make_response
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste123'


@app.route('/')
def home():
    if 'password' in request.cookies:
        if request.cookies['password'] == app.config['SECRET_KEY']:
            return render_template('home.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == app.config['SECRET_KEY']:
            response = make_response(redirect(url_for('home')))
            response.set_cookie('password', password)
            return response
        else:
            return render_template('login.html', error='Senha inválida!')
    else:
        return render_template('login.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    id = request.form['id']
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id])
    return redirect(url_for('home'))


@app.route('/export_csv')
def export_csv():
    if 'password' in request.cookies:
        if request.cookies['password'] == app.config['SECRET_KEY']:
            with open('students.csv', 'r') as file:
                data = file.read()
            response = make_response(data)
            response.headers["Content-Disposition"] = "attachment; filename=students.csv"
            return response
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
