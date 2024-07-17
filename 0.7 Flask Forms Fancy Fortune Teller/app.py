from flask import Flask, render_template,url_for,redirect,request

app = Flask(__name__,
template_folder='templates',
static_folder='static')

# Route for the home page
@app.route('/home',methods=["POST","GET"])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birth = request.form['birth']

        return redirect(url_for('fortune',
                 birth= birth,
                ))

@app.route('/fortune/<string:birth>')
def fortune(birth):
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
    the_value=len(birth)#fortunes[random.randint(0, 9)]
    if the_value < 10:
        return render_template("fortune.html",fortune=fortunes[the_value])
    else:
        return render_template("fortune.html",fortune=fortunes[9])


if __name__ == '__main__':
    app.run(debug=True, port = 5050)

