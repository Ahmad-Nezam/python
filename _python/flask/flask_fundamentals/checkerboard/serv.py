from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def check1(i=8,j=8):
    num_box = int(i)
    num_box = int(j)
    return render_template("index.html", num_box = num_box)


@app.route("/4")
def check2(i=8,j=4):
    num_box = int(i)
    num_box = int(j)
    return render_template("index.html", num_box = num_box)


@app.route("/<string:i>/<string:j>")
def check3(i,j):
    num_box = int(i)
    num_box = int(j)
    return render_template("index.html" , num_box = num_box)



if __name__ == "__main__":
    app.run(debug=True)