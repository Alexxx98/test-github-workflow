from flask import Flask
''' Import flask module '''

app = Flask(__name__)

@app.route('/')
def index():
    ''' printing greetings message to the page. '''
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
