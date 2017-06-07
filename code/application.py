from flask import Flask, flash, redirect, render_template, request, session, url_for,send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
from PIL import ImageFilter
from subprocess import call
import subprocess as sub
import os
import traceback
import sys
from io import StringIO
#from wand.image import Image
import glob
# configure application

UPLOAD_FOLDER ="/home/gurvinder/book_digitisation/code/static"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def index():
    print("helllo.................................")
    return render_template("login.html")
    #return apology("index")
@app.route("/fileupload.html",methods=["GET","POST"])
def fileupload():
    print("..............................hello")
    filepath=""
    filedata=[]
    call(["rm","outfile.txt"])
    file = request.files['file']
    print(file.filename)
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if (file.filename.lower().endswith('.jpg')) or (file.filename.lower().endswith('.png')):
        print("jpg")
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        print(file.filename+"................")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        path=(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        #call(["tesseract", path, "outfile"])
        #process_image(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        print(pytesseract.image_to_string(Image.open(path)),file=open("outfile.txt", "w+"))
        #print(pytesseract.image_to_string(Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))))
        #print(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        file.close()
        filedata=filehandle()
        #return render_template('fileupload.html',filename=os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return render_template('fileupload.html',filename=file.filename,filedata=filedata)
                #return redirect(url_for('uploaded_file', filename=filename))
    elif file.filename.lower().endswith('.pdf'):
        print("pdf........................")
        file = request.files['file']
        print(file.filename + "................")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        print("hello gurvinder")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print(filepath, ".........................")
        p = sub.Popen(['gs', '-dNOPAUSE', '-dBATCH', '-sDEVICE=png16',
                       '-sOutputFile=/home/gurvinder/book_digitisation/code/photos/%d.png', '-r300', filepath],
                      stdout=sub.PIPE, stderr=sub.PIPE)
        filedata = []
        # os.system("cd /home/gurvinder/book_digitisation/code/photos/; ls *.png |cat>result.txt")
        # pdf_page_info=open('/home/gurvinder/book_digitisation/code/photos/result.txt','+r')
        # for page in pdf_page_info:
        filePath = os.getcwd()
        print(filePath)
        # print(glob.glob("filepath*.png"))
        page_info = glob.glob('photos/*.png')
        for count in page_info:
            filePathWithSlash = filePath + "/"
            print(filePathWithSlash)
            filenameWithPath = os.path.join(filePath, count)
            print(filenameWithPath)
            print(filePath, "................")
            # call(["tesseract", filenameWithPath,"outfile"])
            print(pytesseract.image_to_string(Image.open(filenameWithPath)), file=open('output.txt', '+a'))
        filedata = filehandle()
        return render_template('fileupload.html', filedata=filedata)






    else:
        print("hi iam else")
def filehandle():
    print("...file handle....")
    details = []
    with open("output.txt") as file:
        for line in file:
            details.append(line)
        file.close()
        print(details)
    return details

def pdf_to_img():

    #output, errors = p.communicate()
    #print(output)
    #(cd / c; / a / helloworld)
    #call(["cd /home/gurvinder/book_digitisation/code/photos/;","ls", "*.png"])

    filehandle_pdf()
    #os.system("gs -dNOPAUSE -dBATCH -sDEVICE=png16 -sOutputFile=%d.png -r300",filepath)
    #os.system("gs -q -dSAFER  -sDEVICE=png16m -r500 -dBATCH -dNOPAUSE  -dFirstPage=%d -dLastPage=%d -sOutputFile=/xx.png %s" % ( i, i, self.id, i, s.path.join(app.config['UPLOAD_FOLDER'], file.filename)))
    #call(["gs","dNOPAUSE","-dBATCH","-sDEVICE=png16","-sOutputFile=%d" ,"-r300" ,"file.filename"])
def filehandle_pdf():
    page_info=[]


    #filePathWithSlash = filePath + ""
    #print(filePathWithSlash)
        #import pdb
        #pdb.set_trace()
        #filenameWithPath = os.path.join(filePath,page)
        #print(filenameWithPath)
        #call(["tesseract",filenameWithPath,"outfile"])

        #f=open("outfile.txt","+a")

        #p=sub.Popen(['tesseract',filenameWithPath,'outfile'],stdout=sub.PIPE, stderr=sub.PIPE)
        #output, errors = p.communicate()
        #print(output)
        #f.close()
        #print(pytesseract.image_to_string(Image.open(filenameWithPath)),file=open('output.txt','+a'))


#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
 #   print(".........gurvinder")
  #  filename = 'C:/traning/'+ filename
   # return render_template('fileupload.html', filename=filename)
#@app.route('/uploads/<filename>')
#def send_file(filename):
 #   return send_from_directory(UPLOAD_FOLDER, filename)
