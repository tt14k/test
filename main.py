#!/usr/bin/env python
# -*- coding:sjis -*-
from flask import Flask, render_template
import requests

app = Flask(__name__)

#�f�R���[�^�[
#�g�b�v�y�[�W�ɃA�N�Z�X���ꂽ�ꍇ�A������ɃA�N�Z�X
@app.route('/')
def main():
    oshimen = {
        'name' : '�ق񂾂�����',
        'status':'��������'
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