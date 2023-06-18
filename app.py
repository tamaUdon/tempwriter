#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
from flask import Flask, Response
from hands import gesture_recognizer

app = Flask(__name__)

@app.route('/')
def index():
    return Response(gesture_recognizer.execute(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989, debug=True, threaded=True)
