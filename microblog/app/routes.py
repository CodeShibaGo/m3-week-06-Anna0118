from app import app

@app.route('/')
def index():
    return 'Hello world'

@app.route('/about')
def about():
    return '<h1>About</h1>'

if __name__=='__main__':
    app.run()