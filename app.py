from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
    return render_template('welcome.html')



@app.route('/pledgeclass')
def pledgeclass():
    return render_template('pledgeclass.html')


@app.route('/personal')
def personal():
    return render_template('personal.html')




if __name__ == '__main__':
    app.run(debug=True)





