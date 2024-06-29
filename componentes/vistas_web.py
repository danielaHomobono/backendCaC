from flask import render_template
from app import app

# Ejemplo de vista para la página principal
@app.route('/')
def home():
    return render_template('index.html')
