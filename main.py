from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run(debug=True)