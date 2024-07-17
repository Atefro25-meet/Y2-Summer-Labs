from flask import Flask, render_template
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')

# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fortune')
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
    the_value=fortunes[random.randint(0, 9)]
    return render_template("fortune.html",fortune=the_value)



if __name__ == '__main__':
    app.run(debug=True, port = 5050)

