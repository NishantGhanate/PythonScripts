from flask import Flask, render_template, Response ,  redirect , request , url_for
from flask_restful import Resource , Api
import pandas as pd
import socket , os ,datetime


ROOT = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = ROOT + os.sep + 'UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'csv'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


connection = sqlite3.connect(ROOT + os.path.sep + "idrl.db")
crsr = connection.cursor()
sql_command = """ CREATE TABLE IF NOT EXISTS file (
            id INTEGER PRIMARY KEY  AUTOINCREMENT, 
            filepath varchar(255) ,
            timestamp varchar(255) 
            ); """
           
crsr.execute(sql_command)
connection.commit()
query = 'SELECT * FROM Table ORDER BY ID DESC LIMIT 1'


@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        timestamp =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        crsr.execute("INSERT INTO file (filepath , timestamp) VALUES (?,?)",(path,timestamp))
        return redirect(url_for('renderLeadboard'))
    

@app.route('/leaderboard' )
def renderLeadboard():
   
    path = '
    info = pd.read_csv(path)
    return render_template('leaderboard.html', info = info )

if __name__ == '__main__':
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr)
    app.run(host='127.0.0.1',port='5000',debug=True)

    # app.run(host='127.0.0.1' , port='5000' ,threaded=True)
    # https://ngrok.com/download
    # ngrok http 5000 