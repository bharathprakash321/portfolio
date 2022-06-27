from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, request
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html')

def write_to_db(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        spamwriter = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email, subject, message])

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('formsubmitted.html', message = 'Your form has been submitted!!!')
    else:
        return render_template('formsubmitted.html', message = 'We are facing some issue')