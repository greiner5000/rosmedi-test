from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hola Jorge 👋</h1><p>Tu app Flask está corriendo en Render 🚀</p>"

if __name__ == '__main__':
    app.run(debug=True)
