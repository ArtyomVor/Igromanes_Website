from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from os import path
from os import environ
from random import randint
from random import seed
from time import time

# from forms.userForm import LoginForm
# from forms.userForm import RegisterForm
# from forms.userForm import AdminForm
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route("/")
@app.route("/index")
def index():
    params = {}
    params['title'] = "Любимый сайт игроманов =)"
    return render_template("index.html", **params)


def main():
    db_session.global_init("db/Jujutsu_Shenanigans.db")

    # db_fill.Honored_One()

    # db_sess = db_session.create_session()
    # pers = db_sess.query(Character).filter(Character.id==5).first()
    # pers.tips = '''
    # '''
    # db_sess.commit()
    # print(f"{pers.name}: tips updated")

# ---------------------< Дебаг >---------------------
import traceback


@app.errorhandler(500)
def error500(error):
    print(traceback.format_exc())
    return "Ошибка на сервере(500), напишите Богу, и он скоро всё исправит)", 500


@app.errorhandler(404)
def error404(error):
    print(traceback.format_exc())
    return "Страничка не найдена", 404

# ---------------------< Main >---------------------
if __name__ == '__main__':
    main()
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# Добавить html для error 404