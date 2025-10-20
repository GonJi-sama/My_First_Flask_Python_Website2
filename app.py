from flask import Flask, render_template
from mylib import mainfunc as mf
app = Flask(__name__)

@app.route('/')
def home():
    place = "Sydney"
    return render_template('index.html', place=place)

@app.route('/tech')
def tech():
    tech_prefer = "quantum computing"
    return render_template('tech.html', tech_prefer=tech_prefer)

@app.route('/myid')
def myid():
    return "My SID is 68130677"

@app.route('/draw/<int:number>')
def draw(number):
    pattern = mf.myfunc('x', number)
    return f"""<pre style="font-size: 100px; line-height: 1;">{pattern}</pre>"""

@app.route('/sum/<int:x>/<int:y>')
def sumation(x,y):
    sum = x + y
    return f"The result of sum between xx and yy is {sum}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)