from flask import Flask, redirect, url_for, request
app = Flask(__name__)

# Redirect Link after getting input from Form 
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# To get Data from html form use name parameter in html tag 
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)