from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚧 GIP Nube Link GIP</h1><p>Visor Dicom En Construcción🚧</p>"

if __name__ == '__main__':
    app.run(debug=True)


