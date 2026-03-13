from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    
    result = None
    
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        result = num1 + num2

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
