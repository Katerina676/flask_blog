from flask import Blueprint
from flask import render_template
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<id>')
def post_detail(id):
    post = Post.query.filter(Post.id==id).first()
    return render_template('posts/post_detail.html', post=post)