#!/usr/bin/env python
# -*- coding:sjis -*-
from flask import Flask, render_template
import requests

app = Flask(__name__)

#デコレーター
#トップページにアクセスされた場合、こちらにアクセス
@app.route('/')
def main():
    oshimen = {
        'name' : 'ほんだかすみ',
        'status':'だいすき'
    }

    return render_template(
        'main.html',
        oshimen = oshimen
    )

@app.route("/calc")
def calc():
    return render_template('calc.html')

if __name__ == '__main__':
    app.run(debug=True)