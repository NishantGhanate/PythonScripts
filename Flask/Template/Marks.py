from flask import Flask, render_template
app = Flask(__name__)

# e.g 127.0.0.1/marks/65 
# Default is GET
@app.route('/marks/<int:score>' )
def render_result(score):
   return render_template('Marks.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)