from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
def home():
    return 'Hello world'


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET','POST']) #接受 GET 和 POST 請求
def login():
    form = LoginForm()
    #  由flask_wtf提供的method，可以直接確認POST與欄位驗證以及最重要的CSRF
    #  flask_wtf類中提供判斷是否表單提交過來的method，不需要自行利用request.method來做判斷
    if form.validate_on_submit():
        # 登入後會在網頁上呈現 ex, Login requested for user 123, remember_me=False
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # return 'Success Submit'
        return redirect(url_for('index'))
    #  如果不是提交過來的表單，就是GET，這時候就回傳login.html網頁
    return render_template('login.html',  title='Sign In', form=form)

