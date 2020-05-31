import os
from flask import flash, request, redirect, url_for, render_template
from stegano import app
from werkzeug.utils import secure_filename
from stegano.dissimulation_methode import dissimulation_methode2,dissimulation_methode1
import stegano.extraction_methode
from PIL import Image
import time

UPLOAD_FOLDER = 'stegano'
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
    cle = None
    canal = None
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

            if methode == 2 :
                bit = request.form['methode2-bit']
                image_cover = Image.open(UPLOAD_FOLDER+"\\"+filename)
                # pylint: disable=too-many-function-args
                image_stego, canal , cle , psnr = dissimulation_methode2(image_cover, message, bit,canal)
                #image_stego.save(UPLOAD_FOLDER+'\\stego.jpg')
                #image = Image.open(UPLOAD_FOLDER+'\\stego.jpg')
                #message_secret = stegano.extraction_methode.extraction_methode2(image, cle, canal, bit)
                #print(message_secret)


                print(type(canal))
                print(type(cle))
            else:
                image_stego, canal , cle , psnr = dissimulation_methode1(image_cover, message,canal)
                
            #return redirect(url_for('dissimulation'))
            print('canal = '+str(canal))
            print('cle = '+str(cle))
            image_stego.save(UPLOAD_FOLDER+"\\"+'stego.jpg')
            print("it took  :"+ str(time.time() - start) + " seconds.")

    return render_template('index.html', title="dissimulation", filename=filename, result_path=result_path, psnr=psnr, cle=cle, canal=canal)
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
        cle = 32

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image_stego =Image.open(filename)#UPLOAD_FOLDER+'\\'+
            print(filename)
            print(os.getcwd())
            if methode == 2 :
                bit = request.form['methode2-bit']
                # pylint: disable=too-many-function-args
                
                message_secret = stegano.extraction_methode.extraction_methode2(image_stego, cle, canal, bit)
                
            else:
                # pylint: disable=too-many-function-args
                 message_secret = stegano.extraction_methode.extraction_methode1(image_stego, cle, canal)
            
            print(message_secret)

            print('bit :' + str(bit))
            print('le canal a la fin : '+str(canal))
            print('la cle a la fin : '+str(cle))
            print("it took  :"+ str(time.time() - start) + " seconds.")


    return render_template('extraction.html',title="Extraction", filename=filename,message_secret=message_secret )

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    return render_template('evaluation.html')

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template('detail.html')
