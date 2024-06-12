from flask import Flask , render_template ,redirect,session ,request
app = Flask(__name__)
app.secret_key= ' this key is privacy '

@app.route('/')
def count1():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return render_template("index.html")
    

@app.route("/count" , methods=["POST"])
def count2():
    if request.form['alter']=='add':
        session['count'] += 1
    elif request.form['alter']=='reset':
        session['count'] =0
        
    return redirect("/")

@app.route("/destroy")
def count3():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
