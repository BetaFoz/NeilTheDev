from flask import Flask, request, flash, redirect, url_for
from flask_mail import Mail, Message
from app.vars import MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.neilthedev.com'
app.config['MAIL_PORT'] = 465
app.config['MAIl_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['SECRET_KEY'] = 'some_random_key'

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['contact-name']
        email = request.form['contact-email']
        message = request.form['contact-message']

        msg = Message('Contact Us Form Submission', sender='your_email@example.com', recipients=['neil@neilthedev.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        flash('Message sent successfully','success')
    return redirect(url_for('index'))

from app import views
