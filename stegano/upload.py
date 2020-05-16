import os
from flask import flash, request, redirect, url_for, render_template
from stegano import app
from werkzeug.utils import secure_filename
from stegano.image import pfe

UPLOAD_FOLDER = 'D:\Documents\isil L3\S2\PFE\web page\stegano'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@app.route('/dissimulation', methods=['GET', 'POST'])
def dissimulation():
    filename = None
    psnr = None
    bit = None
    result_path = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("sdfsvfs")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        message = " ce message est secret "
        message = request.form['text-secret']
        position= int(request.form['canal'])
        methode = int(request.form['methode'])
        if methode == 2 :
            bit = request.form['methode2-bit']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            # pylint: disable=too-many-function-args
            psnr, image3 = pfe(filename, message, position, UPLOAD_FOLDER, bit)
            result_path = 'image_transform.jpg'
            image3.save(result_path)
            #return redirect(url_for('dissimulation'))

    return render_template('index.html', title="dissimulation", filename=filename, result_path=result_path, psnr=psnr)
@app.route('/extraction', methods=['GET', 'POST'])
def extraction():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("sdfsvfs")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        position= int(request.form['position'])
        methode = int(request.form['methode'])
        if methode == 2 :
            bit = request.form['methode2-bit']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('extraction.html')

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    return render_template('evaluation.html')

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template('detail.html')
