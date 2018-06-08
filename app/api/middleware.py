import jwt
import functools
from flask import current_app, request, jsonify
# from jwt.errors import PyJWTError

def login_required(f):
    @functools.wraps(f)
    def check_login(*args, **kwargs):
            if 'Authorization' in request.headers:
                auth_value = request.headers.get('Authorization')
                if auth_value and 'Bearer ' in auth_value:
                    secret = current_app.config['SECRET_KEY']
                    token = auth_value.split('Bearer ')[1]
                    if not token:
                        return jsonify(message='No token was found for header "Authorization: Bearer <token>"'), 403
                    try:
                        decoded = jwt.decode(token, secret, algorithm='HS256')
                    except Exception as e:
                        return jsonify(message='Failed to decode JWT: {}'.format(e)), 403
                else:
                    return jsonify(message='Authorization header was found but did not follow the required format "Authorization: Bearer <token>"'), 403
            else:
                return jsonify(message='No Authorization header was found.'), 403
            return f(*args, **kwargs)
    return check_login