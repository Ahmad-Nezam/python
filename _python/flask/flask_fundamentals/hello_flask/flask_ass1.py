from flask import Flask ,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return 
@app.route("/dojo")

def hello2():
    return "hi"

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

@app.route("/lists")
def my_list():

    students_info=[
        {'name': 'Ahmad' ,'age':22},
        {'name': 'Salah' ,'age':21},
        {'name': 'Mohammad' ,'age':20},
        {'name': 'Omar' ,'age':19}
    ]
    return render_template("index.html" ,random_numbers=[3,1,5] ,students=students_info ,phrase="hello", times=5 )

if __name__ == "__main__":
    app.run(debug=True) 