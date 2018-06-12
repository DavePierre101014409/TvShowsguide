import os 
import smtplib

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
    students.append()
    
    return redirect("/main")

@app.route("/main")
def main():
    return render_template("main.html",register=register)
if __name__== '__main__':
    app.run(debug=True)
