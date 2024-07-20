from flask import Flask, render_template,url_for,redirect,request
from flask import session as login_session

app = Flask(__name__,
template_folder='templates',
static_folder='static')

app.config['SECRET_KEY'] = "Rotem"

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login_session["username"]= request.form["username"]
        login_session["birth"]=request.form["birthmonth"]
        
        return redirect(url_for("home"))
     
                


@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "GET":
        username = login_session.get("username", "Guest")
        return render_template("home.html", username=username)
    else:
        return redirect(url_for('fortune'))


 
@app.route("/fortune")
def fortune():
    fortunes = [
        "buy an icecream and see",
        "go to the antique shop and see",
        "Today is your lucky day!",
        "go to the cafe and you'll see",
        "stay awake",
        "he will be there",
        "the opportionety is infront of you",
        "treasure",
        "girl friend",
        "nice day"
    ]
    the_value=len(login_session["birth"])#fortunes[random.randint(0, 9)]
    fi_len=int(len(str(the_value))-1)
    let=int((the_value)%(10**fi_len))
    if the_value < 10:
        return render_template("fortune.html",fortune=fortunes[the_value])
    else:
        return render_template("fortune.html",fortune=fortunes[let])


if __name__ == '__main__':
    app.run(debug=True, port = 5050)

