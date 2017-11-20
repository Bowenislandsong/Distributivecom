from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/upload')
def upload_file():
   return render_template('user.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      target = os.path.join(APP_ROOT, 'home/ubuntu/Source/{}'.format(filename))
      destination = "/".join([target])
      f.save(destination)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
