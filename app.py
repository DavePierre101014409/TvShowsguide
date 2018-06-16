import os
import smtplib
import sqlite3

from flask import Flask, render_template, request



app = Flask(__name__)
# registers
register =[]

@app.route("/a")
def getData():
    conn = sqlite3.connect('../users.db')
    curs=conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, fName TEXT, lName TEXT)")

    curs.execute("INSERT INTO user (fName ,lName ) VALUES ('Dave','Dace') ")

    for row in curs.execute("SELECT * FROM user"):
    	time = str(row[0])
    	temp = row[1]
        t = row[2]
        


    	return time + temp+ t

    print str(curs.execute("SELECT fName from user"))

    return str(curs.execute("SELECT * from user"))
    conn.close()







@app.route("/")
def homePage():
    return render_template("home.html")
#    return render_template("Homepage.html")

@app.route("/signIn")
def signPage():
    return render_template("SignInPage.html")

@app.route("/register", methods=["POST"])
def register():
    firstname = request.form.get("")
    lastName = request.form.get("")
    emailName = request.form.get("")
    if not firstname or not lastName or not emailName :
        # return failure
        return render_template("")
    students.append()

    return redirect("/main")

@app.route("/main")
def main():
    return render_template("main.html",register=register)
if __name__== '__main__':
    app.run(debug=True)
