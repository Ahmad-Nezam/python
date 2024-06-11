from flask import Flask ,render_template
app = Flask(__name__)

@app.route("/play")
def show_box1(x=3,color="red"):
    num_box = int(x)
    box_color = color
    return render_template("index.html",num_box = num_box,box_color=box_color)

@app.route("/play/<string:x>/<string:color>")
def show_box2(x,color):
    num_box = int(x)
    box_color = color
    return render_template("index.html", num_box = num_box,box_color = box_color)

if __name__ == "__main__":
    app.run(debug=True)