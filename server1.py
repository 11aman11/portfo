# NOte: it was on server1.py but changed to server2.py so change the flask setting to new server to make it work
import email
from email import message
import csv
from token import NEWLINE
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)

@app.route("/") # pass the username
def my_home():
    #return "<p>Hello, Aman, it's your website!</p>"
    return render_template("index.html")

@app.route("/<string:pageName>") # pass the username
def htmp_page(pageName):
    #return "<p>Hello, Aman, it's your website!</p>"
    return render_template(pageName)

def writeToFile(data):
    with open(r"C:\Users\Aman\Desktop\Coding\python\ZTM-Python\web server\database.txt", mode="a")as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file= database.write(f"\n{email},{subject},{message}")

def writeToCsv(data):
    with open(r"C:\Users\Aman\Desktop\Coding\python\ZTM-Python\web server\database.csv",newline="", mode="a")as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvWriter= csv.writer(database2,delimiter=",",quotechar="'",quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST', 'GET']) # get=send , post=save
def submit_form():
    if request.method=="POST":
        data= request.form.to_dict()
        writeToCsv(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong,try again!"

# @app.route("/submit_form", methods=['POST', 'GET']) # get=send , post=save
# def submit_form():
#     if request.method=="POST":
#         data= request.form.to_dict()
#         writeToFile(data)
#         return redirect("/thankyou.html")
#     else:
#         return "something went wrong,try again!"
# @app.route("/about.html")
# def about():

#     return render_template("about.html")

# @app.route("/contact.html") #
# def work(): #

#     return render_template("contact.html") #