from flask import Flask, request, current_app

api = Flask(__name__)
api.app_context().push()
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

# 21 марта

@api.route('/aboutyou')
def send_about_user_info() :
    return "Привет, твой ip: {}, а используете вы {}".format(request.remote_addr, request.user_agent) 
@api.route('/about')
def send_about_info():
    return "Скрипт сервера хранится в файле {}".format(current_app.name)


if __name__ == "__main__":
    api.run(debug=True)

