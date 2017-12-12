from flask import Flask, render_template, url_for, request, session, redirect
from flask import flash, Markup, send_from_directory
from flask_pymongo import PyMongo
from werkzeug import secure_filename
from validate_email import validate_email
from pymongo import MongoClient
import os
import bcrypt
import subprocess
import shutil
import zipfile

app = Flask(__name__, static_folder = 'static')

app.config['MONGO_DBNAME'] = 'Your DB name'
app.config['MONGO_URI'] = 'Your DB URI'
mongo = PyMongo(app)
client = MongoClient('DB URI')
db=client.YourDBName


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    if 'username' in session:
        return render_template('indexlogout.html')
    return render_template('index.html')

@app.route('/loggedin')
def loggedin():
    if 'username' in session:
        return render_template('userlogout.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('loggedin'))

    message = Markup('Invalid username/password combination')
    flash(message)
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['username']=="" or \
                request.form['pass']=="" or validate_email(request.form['email'], verify=True)==None or validate_email(request.form['email'], verify=True)==False:
                message = Markup('Invalid. Please register again')
                flash(message)
                return render_template('register.html')
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'email' : request.form['email'], 'password' : hashpass})
            session['username'] = request.form['username']
            #return (url_for('index'))
            session.pop('username')
            message = Markup('Registration successful')
            flash(message)
            return render_template('register.html')
        message = Markup('That Username already exists.')
        flash(message)
        return render_template('register.html')
    return render_template('register.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
    if 'username' in session:
        if request.method == 'POST':
            f = request.files['file']
            filename = f.filename
            if filename == '':
                message = Markup('No file selected')
                flash(message)
                return render_template('userlogout.html')
            try:
                os.remove('home/ubuntu/Solution/'+session['username']+'.zip', dir_fd=None)
            except:
                pass
            users = mongo.db.users
            filename = session['username']+'_'+filename
            target = os.path.join(APP_ROOT, 'home/ubuntu/Source/{}'.format(filename))
            destination = "/".join([target])
            f.save(destination)
            #subprocess.call("mv "+filename+" /var/ftp/pub/outgoing/")
            From = "/home/ubuntu/Final_website/home/ubuntu/Source/"
            ff = From + filename
            users.update({"name":session['username']}, {"$push":{"Uploaded file":filename}})
            user = db.users.find_one({"name": session['username']})
            fileexists = user.get('Uploaded file')
            #fileexists = db.users.find_one({"name":session['username'],})
            if fileexists==None or filename not in fileexists:
                users.update({"name":session['username']}, {"$push":{"Uploaded file":filename}})
                #f.save(destination)
                subprocess.call('sudo mv '+ff+' /var/ftp/pub/outgoing/', shell = True)
                message = Markup(f.filename+ ' has been uploaded')
                flash(message)
                return render_template('userlogout.html')
            else:
                message = Markup(f.filename+ ' has already been uploaded')
                flash(message)
                return render_template('userlogout.html')
        message = Markup(f.filename+ ' has been uploaded')
        flash(message)
        return render_template('userlogout.html')
    return render_template('userlogout.html')        

@app.route('/downloader', methods = ['POST'])
def download_file():
    if 'username' in session:
        if request.method == 'POST':
            try:
                shutil.make_archive('/var/ftp/pub/incoming/uploading/dishantp', 'zip', '/var/ftp/pub/incoming/', 'uploading')
                return send_from_directory(directory='/var/ftp/pub/incoming/uploading/', filename = session['username']+'.zip', as_attachment = True)
            except:
                message = Markup('Please wait until your result is ready.')
                flash(message)
                return render_template('userlogout.html')

@app.route('/logout/')
def logout():
    session.pop('username')
    return redirect(url_for('loggedin'))

@app.route('/user/')
def user():
    if 'username' in session:
        return render_template('userlogout.html')
    return render_template('user.html')

@app.route('/choose/')
def choose():
    if 'username' in session:
        return render_template('chooselogout.html')
    return render_template('choose.html')
    
@app.route('/provider/')
def provider():
    if 'username' in session:
        return render_template('providerlogout.html')
    return render_template('provider.html')

@app.route('/aboutus/')
def aboutus():
    if 'username' in session:
        return render_template('aboutuslogout.html')
    return render_template('aboutus.html')

@app.route('/contactus/')
def contactus():
    if 'username' in session:
        return render_template('contactlogout.html')
    return render_template('contact.html')

@app.route('/registerhere')
def registerhere():
    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=80, debug=True)
