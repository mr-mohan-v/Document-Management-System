from flask import Flask, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__,  template_folder='template')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/', methods=['GET'])
def index():
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
    
    user = {'username': 'student'}
    # Main page
    return render_template('user.html', user=user)


