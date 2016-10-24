from flask import *
from mlab import *
from mongoengine import *
app = Flask(__name__)
mlab_connect()

class Post(Document):
    title = StringField()
    content = StringField()
    def to_json(self):
        return jsonify([post.to_json() for post in Post.objects])

@app.route('/')
def hello_world():
    return jsonify(Post.objects[0].to_json())


if __name__ == '__main__':
    app.run()
