from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return('''
        <html><p>Welcome to our gallery </p> <a href='/fst'> food image: </a></html>
        ''')

@app.route('/fst')
def fst():
    return('''
        <html>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtt3aOrfYZ1KnQq4GK0vf9gkNBC07f72UWQ&s'>
        <h2><a href="/home">home</a></h2>
        <h2><a href="/sec">second</a></h2>
        </html>''')

@app.route('/sec')
def sec():
    return('''
        <html>
        <img src='https://images.immediate.co.uk/production/volatile/sites/30/2023/06/Ultraprocessed-food-58d54c3.jpg?quality=90&resize=440,400'>
        <h2><a href="/first">first</a></h2>
        <h2><a href="/thrd">third</a></h2>
        </html>''')
@app.route('/thrd')
def thrd():
    return('''
        <html>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSudTsDqMa_OimGOwDvB5veN7NQ3lyWuhGSVw&s'>
        <h2><a href="/sec">second</a></h2>
        <h2><a href="/home">home</a></h2>
        </html>''')
    
if __name__ == '__main__':
    app.run(debug=True)
