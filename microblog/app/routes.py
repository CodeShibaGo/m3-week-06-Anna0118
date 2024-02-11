from app import app
from flask import render_template


@app.route('/')
def home():
    return 'Hello world'


@app.route('/about')
def about():
    return '<h1>About</h1>'


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Portland 的天氣真好！'
        },
        {
            'author': {'username': 'Susan'},
            'body': '復仇者聯盟電影真的很酷！'
        }
    ]
    return render_template('index.html', title='首頁', user=user, posts=posts)

if __name__ == '__main__':
    app.run()
