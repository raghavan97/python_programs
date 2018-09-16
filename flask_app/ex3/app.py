from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template(
        'index.html', current_time=datetime.datetime.now()
    )

@app.route('/physics')
def physics_page():
    return render_template(
       'physics.html', current_time=datetime.datetime.now() 
    )

@app.route('/maths')
def maths_page():
    return render_template(
       'maths.html', current_time=datetime.datetime.now() 
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
