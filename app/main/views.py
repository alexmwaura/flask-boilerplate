from flask import render_template,request,redirect,url_for
from .import main


@main.route("/")
def index():
    """
    View root function that returns the index page and its data
    """
    title = 'test'
    return render_template("index.html",title = title,) 




    


       

  

    

            