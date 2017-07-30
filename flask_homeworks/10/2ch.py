from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template


app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',
    SERVER_NAME='127.0.0.1:4000',
    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///2ch.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(3))
    text = db.Column(db.String(10))
    #pub_date = db.Column(db.DateTime, nullable=False)

    def __str__(self, title, text):
        id = self.id
        title = self.title
        text = self.text


from flask_wtf import FlaskForm
from wtforms import StringField, validators
class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=25)
    ])

    text = StringField(label='Text', validators=[
        validators.Length(min=10, max=2500)
    ])


@app.route('/')
def index():
    out = ''
    for post in Post.query.all():
        out += '{}:{}:{}'.format(post.id, post.title, post.text)
#    if Post.query.all()
    #return Post.query.all()
    return out

from datetime import datetime
@app.route('/new', methods=['POST'])
def new_post():
    form = PostForm(request.form)

    print(type(form.title.data), form.text.data)
    p = Post(
             title=form.title.data,
             text=form.text.data)
    db.session.add(p)
    db.session.commit()
    #if request.method == 'POST':\
    return '+'

@app.route('/rmrf')
def rmrf():
    Post.query.delete()
    db.session.commit()
    return '+'

if __name__ == '__main__':
    db.create_all()


app.run()