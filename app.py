from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


#Rerouting pages 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT pledge_class FROM members')
    pledge_classes = [row[0] for row in cursor.fetchall()]  # Get a list of pledge class names
    conn.close()
    return render_template('welcome.html', pledge_classes=pledge_classes)

@app.route('/pledgeclass/<string:pledge_class>') 
def pledgeclass(pledge_class):
    conn = get_db_connection()
    members = conn.execute(
        'SELECT * FROM members WHERE pledge_class = ?', (pledge_class,)
    ).fetchall()
    conn.close()
    # Pass the pledge_class to the template
    return render_template('pledgeclass.html', members=members, pledge_class=pledge_class)

@app.route('/personal/<int:member_id>')  
def personal(member_id):
    conn = get_db_connection()
    member = conn.execute(
        'SELECT * FROM members WHERE id = ?', (member_id,)
    ).fetchone()

    # Access pledge_class using the column name as a key
    pledge_class = member['pledge_class']
    conn.close()
    return render_template('personal.html', member=member, pledge_class=pledge_class)

#database operations
def get_db_connection():
    conn = sqlite3.connect('src/Database/fraternity.db')
    conn.row_factory = sqlite3.Row  
    return conn


if __name__ == '__main__':
    app.run(debug=True)





