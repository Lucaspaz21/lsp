from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] ='27f9967b590bac6bfe0a7c32eacc85d4'
app.config['UPLOAD_FOLDER'] = 'static/files'

from lsp import routes