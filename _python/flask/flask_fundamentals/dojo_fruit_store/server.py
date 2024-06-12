from flask import Flask, render_template, request
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(f"{request.form['strawberry']}")
    print(f"{request.form['raspberry']}")
    print(f"{request.form['apple']}")
    print(f"{request.form['first_name']}")
    print(f"{request.form['last_name']}")
    print(f"{request.form['student_id']}")
    return render_template("checkout.html" , stra = request.form['strawberry'] ,
                           rasp = request.form['raspberry'],
                            app = request.form['apple'],
                             fs = request.form['first_name'], 
                             ls = request.form['last_name'],
                             idd = request.form['student_id'])
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    