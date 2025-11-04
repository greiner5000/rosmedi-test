from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚧 DICOM Link GIP</h1><p>En Construcción🚧</p>"

if __name__ == '__main__':
    app.run(debug=True)

