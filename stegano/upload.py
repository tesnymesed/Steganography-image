import os
from flask import flash, request, redirect, url_for, render_template, send_file
from stegano import app
from werkzeug.utils import secure_filename
from stegano.dissimulation_methode import dissimulation_methode2,dissimulation_methode1
import stegano.extraction_methode
from stegano.filter import gaussian_blur,median_filter
from stegano.psnr_mse import calculate_psnr
from PIL import Image
import time
from stegano.redimension import redimensioner2, redimensioner
from random import random

UPLOAD_FOLDER = 'stegano/static/img'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png','gif','bmp'}
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@app.route('/dissimulation', methods=['GET', 'POST'])
def dissimulation():
    
    filename = None
    psnr = None
    cle_cryptage = None
    cle_insertion = None
    canal = None
    canal_name = None
    result_stego = None
    mse = None
    if request.method == 'POST':
        start = time.time()
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        message = " ce message est secret "
        message = request.form['text-secret']
        print("le message est : "+ message)
        canal = int(request.form['canal'])
        methode = int(request.form['methode'])
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            image_cover = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # image_width = image_cover.width 
            # image_height= image_cover.height
            #image_cover = redimensioner2(image_cover,150,150)
            if methode == 2 :

                cle_cryptage = int(request.form['input-case'])
                
                # pylint: disable=too-many-function-args
                image_stego, canal , cle_insertion , psnr , mse = dissimulation_methode2(image_cover, message, cle_cryptage,canal)  
                #message_secret = stegano.extraction_methode.extraction_methode2(image_stego, cle_insertion, canal, cle_cryptage)
                #print(message_secret)

            else:
                image_stego, canal , cle_insertion , psnr , mse = dissimulation_methode1(image_cover, message,canal)
            

            if canal == 0: 
                canal_name = 'Y'
            elif canal == 1:  
                canal_name ='Cb'
            else :
                canal_name ='Cr'


            #return redirect(url_for('dissimulation'))
            print('clé cryptage = '+str(cle_cryptage))
            print('canal = '+str(canal_name))
            print("cle d'insertion ="+str(cle_insertion))
            result_stego = filename+'_stego.png'
            #image_stego = redimensioner2(image_stego, image_width, image_height)
            image_stego.save(os.path.join(app.config['UPLOAD_FOLDER'], result_stego), optimize=True, quality=100)
            print("it took  :"+ str(time.time() - start) + " seconds.")

    return render_template('index.html', title="dissimulation", filename=filename, result_stego=result_stego , psnr=psnr, mse=mse, canal_name=canal_name, cle_cryptage=cle_cryptage, cle_insertion=cle_insertion)
@app.route('/extraction', methods=['GET', 'POST'])
def extraction():
    filename = None
    bit = None
    cle = None
    canal = 2
    message_secret = None
    if request.method == 'POST':

        start = time.time()
        # check if the post request has the file part
        if 'file' not in request.files:
            print("sdfsvfs")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        canal= int(request.form['canal'])
        
        methode = int(request.form['methode'])
        cle = int(request.form['cle_insertion'])
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image_stego =Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            print(os.getcwd())
            if methode == 2 :
                bit = request.form['input-case']
                # pylint: disable=too-many-function-args
                
                message_secret = stegano.extraction_methode.extraction_methode2(image_stego, cle, canal, bit)
                
            else:
                # pylint: disable=too-many-function-args
                image_stego = redimensioner(image_stego)
                message_secret = stegano.extraction_methode.extraction_methode1(image_stego, cle, canal)
            
            print(message_secret)
            
            print('bit :' + str(bit))
            print('le canal a la fin : '+str(canal))
            print('la cle a la fin : '+str(cle))
        print("it took  :"+ str(time.time() - start) + " seconds.")


    return render_template('extraction.html',title="Extraction", filename=filename,message_secret=message_secret)

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    filter = None
    filter_par = None
    filename=None
    result_compression=None
    psnr=None
    mse=None

    if request.method == 'POST':

        start = time.time()
        # check if the post request has the file part
        if 'file' not in request.files:
            print("sdfsvfs")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        filter= int(request.form['filter'])

        filter_par = int(request.form['input-case'])
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image =Image.open(UPLOAD_FOLDER+'\\'+filename)
            chemain_image = UPLOAD_FOLDER+'\\'+filename
            if filter == 0:
                image_filtre = gaussian_blur(chemain_image,filter_par)
                psnr, mse = calculate_psnr(image,image_filtre)
            elif filter == 1:
                image_filtre = median_filter(chemain_image,filter_par)
                psnr, mse = calculate_psnr(image,image_filtre)
            result_compression='filtre.png'
            image_filtre.save(UPLOAD_FOLDER+'\\'+result_compression)
        print("it took  :"+ str(time.time() - start) + " seconds.")

    return render_template('evaluation.html', title="Evaluation",filename=filename, result_compression=result_compression, psnr=psnr, mse=mse)

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template('detail.html')

@app.route('/download/<result_stego>')
def download(result_stego):
    path1 = os.path.join('..',app.config['UPLOAD_FOLDER'])
    path2 = os.path.join(path1, result_stego)
    return send_file(path2, as_attachment=True)