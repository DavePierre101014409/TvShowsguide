import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("Homepage.html")


#def signPage():
#    return render_template("SignInPage.html)
