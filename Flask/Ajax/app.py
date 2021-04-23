from flask import Flask, jsonify, render_template, request
from flask_restful import Resource , Api
import time
import pyautogui

app = Flask(__name__)

# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(100, 150)
# pyautogui.click()
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    pyautogui.moveTo(500, 550)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)