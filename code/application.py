from flask import Flask, flash, redirect, render_template, request, session, url_for,send_from_directory
from flask_session import Session
import os
from werkzeug.utils import secure_filename
# configure application
UPLOAD_FOLDER ="C:/traning/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")

def index():
    print("helllo.................................")
    return render_template("login.html")
    #return apology("index")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/fileupload.html",methods=["GET","POST"])
def fileupload():
    print("..............................hello")
    if request.form['start'] == "start":
    # check if the post request has the file part
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        print(file.filename+"................")
        if file.filename== '':
                flash('No selected file')
                return redirect(request.url)
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print("...........")
                print(filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #return render_template('fileupload.html',filename=filename)
                #return redirect(url_for('fileupload.html',filename=filename))
                return redirect(url_for('uploaded_file', filename=filename))


    if request.form['start']=="start1":
        print("start...........")
        print(request.form['file'])
    elif request.form['cancel']=="cancel":
        print("cancel...........")
    elif request.__form['delete']=="delete":
        print("delete...........")
    else:
        print("hi iam else")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(".........gurvinder")
    filename = 'C:/traning/'+ filename
    return render_template('fileupload.html', filename=filename)
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

