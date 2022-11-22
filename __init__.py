from flask import Flask, render_template, flash, redirect
#from gevent.pywsgi import WSGIServer
from config import Config

app = Flask(__name__,  template_folder='template')
app.config.from_object(Config)

import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    # Serve the app with gevent
    app.run(host='0.0.0.0')
    #http_server = WSGIServer(('0.0.0.0', 5000), app)
    print("Server is running")
    # http_server.serve_forever()
