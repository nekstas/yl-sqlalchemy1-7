# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data.db_session import create_session
from data.users import User

# TODO этот файл


put_parser = reqparse.RequestParser()
put_parser.add_argument('surname')
put_parser.add_argument('name')
put_parser.add_argument('age', type=int)
put_parser.add_argument('position')
put_parser.add_argument('speciality')
put_parser.add_argument('address')
put_parser.add_argument('email')
put_parser.add_argument('hashed_password')
put_parser.add_argument('modified_date')


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"News {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        return jsonify({
            'user': user.to_dict(only=(
                'address', 'age', 'email', 'id', 'modified_date',
                'name', 'position', 'speciality', 'surname'
            ))
        })

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)

        # print(parser.parse_args())

        session.merge(user)
        session.commit()
        return jsonify({'success': 'OK'})
