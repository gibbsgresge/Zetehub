from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


#Rerouting pages 
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


#database operations
def get_db_connection():
    conn = sqlite3.connect('fraternity.db')
    conn.row_factory = sqlite3.Row  # For easy dictionary-like access
    return conn

@app.route('/personal/<int:member_id>')
def personal(member_id):
    conn = get_db_connection()
    member = conn.execute(
        'SELECT * FROM members WHERE id = ?', (member_id,)
    ).fetchone()
    conn.close()
    return render_template('personal.html', member=member)







if __name__ == '__main__':
    app.run(debug=True)





