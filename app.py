import os 
import smtplib
import csv

from flask import Flask, render_template, request 

app = Flask(__name__)
# registers 
register =[]
@app.route("/")
def homePage():
    return render_template("Homepage.html")

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
    message = "You are registered "
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("Dave email adress", os.getenv("PASSWORD"))
    server.sendmail("Same thing",emailName,message)
    students.append()
    
    return redirect("/main")
    
    file= open("registants.csv", "a")
    writer =csv.writer(file)
    writer.writerow((request.form.get(""), request.form.get("")))
    file.close()
    return render_template("sucess.html")
    

@app.route("/main")
def main():
    return render_template("main.html",register=register)
if __name__== '__main__':
    app.run(debug=True)
