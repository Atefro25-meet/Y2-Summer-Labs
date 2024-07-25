from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__,
template_folder='templates',
static_folder='static')



firebaseConfig = {
  "apiKey": "AIzaSyAUgefmHcWN7j5Xn5dLIdt9Pign-GYW6SU",
  "authDomain": "authentication-lab-2f06f.firebaseapp.com",
  "projectId": "authentication-lab-2f06f",
  "storageBucket": "authentication-lab-2f06f.appspot.com",
  "messagingSenderId": "210329119343",
  "appId": "1:210329119343:web:38df5befdd04aa3e34bb9a",
  "measurementId": "G-3XR51JL53N",
  "databaseURL":"https://authentication-lab-2f06f-default-rtdb.europe-west1.firebasedatabase.app/"
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
        
        
        try:
            print(email , password)
            login_session["user"] = auth.create_user_with_email_and_password(email, password)
            login_session["quotes"]= []
            user={"email":email,"fullname":fullname,"username":username}
            uid=login_session['user']['localId']
            db.child("User").child(uid).set(user)
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
        email = request.form["email"]
        password = request.form["password"]
        quotes=[]
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "regestering failed failed"

    else:
        return render_template("signin.html")



@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        text=request.form["quotes"]
        atef=request.form["wroteby"]
        quote={"text":text,"saidby":atef,'uid':login_session['user']['localId']}
        db.child("quotes").push(quote)
        login_session.modified=True
        return redirect(url_for("thanks"))
    else:
        
        return render_template("home.html")

@app.route('/display')
def display():
    login_session.modified=True
    uid=login_session['user']['localId']
    quotes = db.child("quotes").get().val()

    return render_template("display.html",quotes=quotes)

@app.route('/thanks')
def thanks():   
    return render_template("thanks.html")


if __name__ == '__main__':
    app.run(debug=True, port = 5050)

