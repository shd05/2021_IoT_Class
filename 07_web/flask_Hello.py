from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return'''
    
    <p>Hello, Flask!</p>
    <a href="/first">Go first</a>
    <a href="/Second">Go Second</a>    
    
    ''' 

@app.route("/first")
def first():
    return '''
    <p>first Page</p>
    <a href="/">Go Home</a>    
    
    '''


@app.route("/Second")
def Second():
    return'''
    <p>Second Page</p>
    <a href="/">Go Home</a>        
    
    '''    

if __name__ == "__main__":
    app.run(host="0.0.0.0")
