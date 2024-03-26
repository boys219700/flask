from flask import Flask,render_template,request
import pickle
from flask import Flask, request, jsonify
# from model_files.model1 import predict
from model import predict
app = Flask('app')

@app.route("/", methods = ["GET","POST"])
def submit():
    name=''
    if request.method=='POST':
        print(name)
        name=request.form['username']
    return render_template("index.html",name=len(name))
# if __name__ == '__main__':
#     app.run(debug=True)
