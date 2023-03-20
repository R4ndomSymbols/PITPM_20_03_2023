from flask import Flask

api = Flask(__name__)

@api.route('/')
def index():
    return 'Hello World'

@api.route('/user/<id>')
def user_profile(id):
    print(id)
    return "Profile page of user #{}".format(id)


@api.route('/books/<genre>')
def books(genre):
    return "All Books in {} category".format(genre)

if __name__ == "__main__":
    api.run(debug=True)

