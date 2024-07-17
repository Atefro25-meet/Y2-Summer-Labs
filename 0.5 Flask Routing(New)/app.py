from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return("<html><p>Welcome to our gallary </p> <a href='/fst'> house image: </a></html>")

@app.route('/fst')
def fst():
    return("<html><a href='/sec'> pet image: </a><img src='food.jpeg'></html>")

@app.route('/sec')
def sec():
    return("<html><a href='/thrd'>home image:></a><img src='pet.jpeg'></html>")

@app.route('/thrd')
def thrd():
    return("<html><a href='/home'>main page:</a><img src='home.jpeg' > </html>")

    
if __name__ == '__main__':
    app.run(debug=True,port = 5050)
