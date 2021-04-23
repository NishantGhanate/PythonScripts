from flask import Flask, render_template
app = Flask(__name__)

# e.g 127.0.0.1/Person1/JAjajjaa/Person2
# Default is GET
@app.route('/Greetings/<From>/<Message>/<To>' )
def render_greeting(From,Message,To):
   return render_template('Greetings.html', From = From , Message = Message, To=To )

if __name__ == '__main__':
   app.run(debug = True)