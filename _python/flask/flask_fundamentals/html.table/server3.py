from flask import Flask , render_template
app = Flask(__name__)

@app.route("/table")
def tbl():
    student_info=[
                  {'fsname':'Michael', 'lsname' : 'Choi'     , 'fullname' : 'Michael Choi'},
                  {'fsname':'John'  ,  'lsname' : 'Supsupin' , 'fullname' : 'John Supsupin'},
                  {'fsname':'Mark'  ,   'lsname': 'Guillen'  , 'fullname' : 'Mark Guillen'}
    ]
    return render_template("table.html",tbl=student_info)


if __name__ == "__main__":
    app.run(debug=True)