from flask import Blueprint, jsonify, request, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app.model import User
from app.persistence import UserDAO, connection_manager
from app.api.middleware import login_required
from app.persistence.errors import EmailAlreadyExistsError

import jwt
import datetime
import base64

dao = UserDAO(connection_manager=connection_manager)
api = Blueprint('users', __name__)

@api.route('/', methods=['GET'])
@login_required
def get_all():
    return 'All users'


@api.route('/', methods=['POST'])
def register_user():
    try:
        req_body = request.get_json()
        user = User.from_json(**req_body)
        user.password = generate_password_hash(user.password)
        dao.insert(user)
        return jsonify(user.json())
    except EmailAlreadyExistsError as e:
        return jsonify(message='This email is already in use.'), 409


@api.route('/login', methods=['POST'])
def login():
    req_body = request.get_json()
    user = dao.get_by_email(req_body['email'])
    if not user:
        return jsonify(message='No account was found for email {}'.format(req_body['email']))

    if check_password_hash(user.password, req_body['password']):
        secret = current_app.config['SECRET_KEY']
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        payload = {
            'iss': current_app.config['ISSUER'],
            'sub': current_app.config['SUBJECT'],
            'exp': exp.timestamp(),
            'userId': user.id
        }
        current_app.logger.info('payload to encode {}'.format(payload))
        try:
            encoded_token = jwt.encode(payload, secret, algorithm='HS256')
            token = encoded_token.decode()
            return jsonify(message='Successfully created token.', token=token)
        except Exception as e:
            return jsonify(message='Failed to create access token: {}'.format(e)), 500
    else:
        return jsonify(message='Invalid email and password combination.'), 400


