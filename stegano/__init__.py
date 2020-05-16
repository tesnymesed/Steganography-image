from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY']='d041467b9e87b0efc0dae083fb3197f4'



from stegano import upload
