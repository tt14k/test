from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/option')
def main():
    return render_template('option.html')

if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run(debug=True)