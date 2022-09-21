from flask import Flask, render_template, url_for, session, redirect, request
from dotenv import load_dotenv
import sqlite3
import os
import json

# take environment variables from .env
load_dotenv()  

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_KEY").encode("utf-8")

def MakeDict(keys, values, len):
    res = {}
    for idx in range(len):
        res[keys[idx]] = values[idx]
    return res

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if 'PersonID' in session:
        return 'Already Logged In', 400

    # Look for user and password in database
    con = sqlite3.connect("muzenkab.db")
    cur = con.cursor()
    PersonID = cur.execute(f"SELECT PersonID FROM users WHERE Username='{request.form['Username']}' AND Password='{request.form['Password']}';").fetchone()[0]
    con.close()
    
    if PersonID:
        session['PersonID'] = PersonID
        print('Login Successful')
        return 'Login Successful', 200
    else:
        print('Login Failed')
        return 'Login Failed', 401

@app.route('/logout', methods=['POST'])
def logout():
    # Logout from session
    session.pop('PersonID', None)
    return 'Logout Successful', 200

@app.route('/signup', methods=['POST'])
def signup():
    con = sqlite3.connect("muzenkab.db")
    cur = con.cursor()
    PersonID = cur.execute(f"SELECT PersonID FROM users WHERE Username='{request.form['Username']}';").fetchall()
    print(PersonID)

    if PersonID:
        con.close()
        return 'User Already Exists', 400

    try:
        cur.execute(f"INSERT INTO users (FirstName, LastName, Username, Password, CellPhone, Email) VALUES ('{request.form['FirstName']}', '{request.form['LastName']}', '{request.form['Username']}', '{request.form['Password']}', '{request.form['CellPhone']}', '{request.form['Email']}');")
        con.commit()
    except:
        return 'Invalid Entry', 401

    con.close()
    return 'Created Successfuly', 200

@app.route('/user/<Username>', methods=['GET'])
def profile(Username):
    con = sqlite3.connect("muzenkab.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    try:
        PersonID = cur.execute(f"SELECT * FROM users WHERE Username='{Username}';").fetchone()
        con.close()
        res = MakeDict(PersonID.keys(), PersonID, len(PersonID.keys()))
        return json.dumps(res), 200
    except:
        return 'User not found', 400

@app.route('/editUser', methods=['POST'])
def editUser():
    con = sqlite3.connect("muzenkab.db")
    cur = con.cursor()
    PersonID = cur.execute(f"SELECT PersonID FROM users WHERE Username='{request.form['Username']}' AND Password='{request.form['OldPassword']}';").fetchone()

    if PersonID:
        try:
            cur.execute(f"UPDATE users SET FirstName='{request.form['FirstName']}', LastName='{request.form['LastName']}', CellPhone='{request.form['CellPhone']}', Email='{request.form['Email']}', Password='{request.form['NewPassword']}' WHERE PersonID='{PersonID[0]}'")
            con.commit()
        except:
            return 'Invalid Entry', 401
        con.close()
        return 'Updated User', 200
    else:
        con.close()
        return 'No Matching User', 400

@app.route('/joinParty', methods=['POST'])
def joinParty():
    if 'PersonID' in session:
        
        con = sqlite3.connect("muzenkab.db")
        cur = con.cursor()

        Persons = cur.execute(f"SELECT PersonID0, PersonID1, PersonID2, PersonID3, PersonID4, PersonID5, PersonID6, PersonID7, PersonID8, PersonID9 FROM parties WHERE PartyID='{request.form['PartyID']}'" ).fetchone()
        if session['PersonID'] in Persons:
            return 'User Already in Party', 401

        space = None
        for idx in range(10):
            if bool(Persons[idx] == None):
                space = idx
                break
        
        if bool(space==None):
            return 'No Space Available In Party', 402

        Parties = cur.execute(f"SELECT PartyID1, PartyID2, PartyID3, PartyID4, PartyID5 FROM users WHERE PersonID='{session['PersonID']}'" ).fetchone()

        for idx in range(5):
            if bool(Parties[idx] == None):
                cur.execute(f"UPDATE users SET PartyID{idx+1}='{request.form['PartyID']}' WHERE PersonID='{session['PersonID']}'")
                cur.execute(f"UPDATE parties SET PersonID{space}='{session['PersonID']}' WHERE PartyID='{request.form['PartyID']}'")
                con.commit()

        cur.close()
            

        return f"Added {session['PersonID']} successfuly to {request.form['PartyID']}", 200
        
    return 'No User in Session', 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
