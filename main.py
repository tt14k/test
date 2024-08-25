from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run(debug=True)