from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'great number' 

@app.route('/', methods=['POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['message'] = ''
        

    if request.method == 'POST':
        guess = int(request.form['guess'])
      
        if guess < session['number']:
            session['message'] = 'Too low!'

        elif guess > session['number']:
            session['message'] = 'Too high!'

    
    return render_template('great_number.html', message=session.get('message', ''))

@app.route('/reset')
def reset():
    session.pop('number', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
