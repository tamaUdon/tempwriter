#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, get_template_attribute
import js2py

from hands import gesture_recognizer as hands

app = Flask(__name__)
# registrar = MyObjectRegistrar(app)

@app.route('/')
def index():
    return Response(hands.gesture_(),mimetype='multipart/x-mixed-replace; boundary=frame')
    # TODO: 後でプリンター画面とくっつける（いるのか？）
    #return render_template('index.html')

# def printer():
#     #if registrar.get("printer"):
#     # printer_ = registrar.get("printer")
#     # print(f"printer={printer_}")
#     with app.app_context():
#         printer_ = get_template_attribute('index.html', 'printer')
#         printer_('World')
#     #return render_template('index.html', printText='True')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989, debug=True, threaded=True)