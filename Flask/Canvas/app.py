from flask import Flask, jsonify, render_template, request
from flask_restful import Resource , Api
import time
import pyautogui

app = Flask(__name__)

# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(100, 150)
# pyautogui.click()
@app.route('/windows')
def open():
    a = request.args.get('start', 0, type=int)
    pyautogui.moveTo(100, 150)
    pyautogui.press('f12')
    pyautogui.hotkey('ctrl','tab')
    pyautogui.hotkey('ctrl', 'shift', 'esc')
    return jsonify(result=a)

@app.route('/blinkyboi')
def moveIt():
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)
    pyautogui.moveTo(x, y)
    return jsonify(result=x)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    # https://pyautogui.readthedocs.io/en/latest/keyboard.html