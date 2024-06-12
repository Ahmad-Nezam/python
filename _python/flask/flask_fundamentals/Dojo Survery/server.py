from flask import Flask , render_template , request ,redirect
app = Flask(__name__)

@app.route("/")
def showing():
    return render_template("index.html")


@app.route('/result' , methods=['POST'])
def dojo():
    print("got post info")
    print(request.form)
    print(f"name submitted :  {request.form['name']}")
    print(f"location submitted :  {request.form['loc']}")
    print(f"language submitted :  {request.form['lang']}")
    print(f"comment submitted :  {request.form['com']}")

    return render_template("info.html" ,name =request.form['name'] ,location = request.form['loc'] 
                           , language = request.form['lang'],
                             comment = request.form['com'])
                          




if __name__ == "__main__":
    app.run(debug=True) 