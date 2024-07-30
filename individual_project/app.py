from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__,
template_folder='templates',
static_folder='static')


firebaseConfig = {
  "apiKey": "AIzaSyBSVH2MKyUbXp9Dpv6ZBHhgsZeDoc7eB7s",
  "authDomain": "personal-project-79900.firebaseapp.com",
  "databaseURL": "https://personal-project-79900-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "personal-project-79900",
  "storageBucket": "personal-project-79900.appspot.com",
  "messagingSenderId": "238842103072",
  "appId": "1:238842103072:web:6d56f341f58f7239e58345",
  "measurementId": "G-5RE4GDWBZX",
  "databaseURL":"https://personal-project-79900-default-rtdb.europe-west1.firebasedatabase.app/"
}




firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()

app=Flask(__name__ , template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = "super-secret-key"



@app.route('/',methods=["POST","GET"])
def signup():
    error = ""

    if request.method == "POST":
      email = request.form["email"]
      password = request.form["password"]
      fullname = request.form["fullname"]
      username = request.form["username"]
      # get_spend=login_session["get_spend"]
      # what_type=login_session["what_type"]
      # how_much=login_session["how_much"]
      login_session["username"]= username
      inv_bu=0
      own_bu=0
      bells_bu=0
      # transactions = {"get_spend":login_session["get_spend"] ,
      #               "what_type":login_session["what_type"],
      #               "how_much":login_session["how_much"]}

      login_session["inv_bu"]=inv_bu
      login_session["own_bu"]=own_bu
      login_session["bells_bu"]=bells_bu

        
      try:
          print(email , password)
          user = auth.create_user_with_email_and_password(email, password)
          login_session["user"] = user
          user={"email":email,"fullname":fullname,"username":username,"inv_bu":0,"own_bu":0,"bells_bu":0}
          uid=login_session['user']['localId']
          db.child("User").child(uid).set(user)
          # transactions = {"get_spend":login_session["get_spend"] ,
          #           "what_type":login_session["what_type"],
          #           "how_much":login_session["how_much"]}
          uid=login_session['user']['localId']
          print("uid",uid)        
          #db.child("Transactions").child(uid).push(transactions)
          login_session["transactionsf"]=db.child("Transactions").child(uid).get().val()
          
          return redirect(url_for("home"))
      except Exception as e:

          error = "regestering failed failed"
          print (e)
          return render_template("signup.html")
    else:
        return render_template("signup.html")


@app.route('/signin',methods=["POST","GET"])
def signin():
    error = ""
    if request.method == "POST":
      login_session = {}
      email = request.form["email"]
      password = request.form["password"]
      
      try:
          user = auth.sign_in_with_email_and_password(email, password)
          login_session['user'] = user
          print(login_session['user'])
          return redirect(url_for('home'))
      except Exception as e:
          error = "regestering failed failed"

          return render_template("error.html")
    else:
        return render_template("signin.html")


@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        login_session.modified=True
        return redirect(url_for("thanks"))
    else:
        
        return render_template("home.html" , usernames= login_session["username"], bells= login_session["bells_bu"],own=login_session["own_bu"],inv= login_session["inv_bu"],)


@app.route('/edit',methods=["POST","GET"])
def edit():
    error = ""
    
    if request.method == "POST":
        login_session["how_much"]=int(request.form["how_much"])
        login_session["get_spend"]=request.form["get_spend"]
        login_session["what_type"]=request.form["what_type"]
        print(login_session["what_type"])
        print(login_session["get_spend"])
        print(login_session["how_much"])


        if login_session["get_spend"] == "get" and login_session["what_type"]=="invest":
          login_session["inv_bu"]+=login_session["how_much"]
          print(login_session["what_type"])
          print(login_session["get_spend"])
          print(login_session["how_much"])
          print("test")
        elif login_session["get_spend"] == "spend" and login_session["what_type"]=="invest":
          login_session["inv_bu"]=login_session["inv_bu"] - login_session["how_much"]


        if login_session["get_spend"] == "get" and login_session["what_type"]=="own":
          login_session["own_bu"]=login_session["own_bu"] + login_session["how_much"]
        elif login_session["get_spend"] == "spend" and login_session["what_type"]=="own":
          login_session["own_bu"]=login_session["own_bu"] - login_session["how_much"]       


        if login_session["get_spend"] == "get" and login_session["what_type"]=="bells":
          login_session["bells_bu"]=login_session["bells_bu"] + login_session["how_much"]
        elif login_session["get_spend"] == "spend" and login_session["what_type"]=="bells":
          login_session["bells_bu"]=login_session["bells_bu"] - login_session["how_much"]
        
        transactions = {"get_spend":login_session["get_spend"] ,
                      "what_type":login_session["what_type"],
                      "how_much":login_session["how_much"]}

        uid=login_session['user']['localId']
        print("uid",uid)        
        db.child("Transactions").child(uid).push(transactions)
        login_session["transactionsf"]=db.child("Transactions").child(uid).get().val()
        return render_template("edit.html")

        
        return render_template("history.html")

    else:
        return render_template("edit.html")   

@app.route('/history', methods=["POST", "GET"])
def history():
    if request.method == "POST":
      login_session.modified=True
      return redirect(url_for("history"))
    else:
      print(login_session)
      uid=login_session['user']['localId']
      print(uid)
      print(login_session["transactionsf"])
      return render_template("history.html",what_types=login_session["what_type"],how_muchs=login_session["how_much"],get_spends=login_session["get_spend"],transactionsfs=db.child("Transactions").child(uid).get().val() , usernames= login_session["username"], howmuch=login_session["how_much"] ,getspend=login_session["get_spend"],whattype= login_session["what_type"],)

@app.route('/error', methods=["POST", "GET"])
def error():
    if request.method == "POST":
        login_session.modified=True
        return redirect(url_for("error"))
    else:
        
        return render_template("error.html")

@app.route('/signout')
def signout():
    login_session['user'].pop()
    auth.current_user = None
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
