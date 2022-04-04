# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from flask import Flask, render_template
from flask_restful import Api

from api import jobs_api, users_resource
from data import db_session
from data.db_session import create_session
from data.jobs import Jobs

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'mars_secret_key'


@app.route('/')
def index():
    with create_session() as session:
        jobs = session.query(Jobs).all()

        return render_template('jobs_list.html', jobs=jobs)


def main():
    db_session.global_init('db/mars.db')

    # api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

    app.register_blueprint(jobs_api.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()

