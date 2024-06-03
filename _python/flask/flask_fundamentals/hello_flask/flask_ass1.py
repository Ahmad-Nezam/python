from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/dojo")
def hello2():
    return "Dojo!"

@app.route("/say/<name>")
def hello3(name):
    print(name)
    return "hi "+name

@app.route("/say/<name>")
def hello4(name):
    print(name)
    return "hi "+name

@app.route("/say/<name>")
def hello5(name):
    print(name)
    return "hi "+name

@app.route("/repeat/<num>/<name>")
def repeat_hello(num,name):
    return f"{name}\n\n"  * int(num)


@app.route("/repeat/<num>/<name>")
def repeat_bye(num,name):
    return f"{name}\n\n"  * int(num)


@app.route("/repeat/<num>/<name>")
def repeat_dogs(num,name):
    return f"{name}\n\n"  * int(num)





if __name__ == "__main__":
    app.run(debug=True) 