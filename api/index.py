from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__, 
            template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates')),
            static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../static')))

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)