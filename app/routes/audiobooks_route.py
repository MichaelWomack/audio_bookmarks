from flask import Blueprint, request, jsonify
from app.persistence.audiobook_dao import AudiobookDAO
from app.config.app_config import Config

config = Config()
dao = AudiobookDAO(config)
audiobooks = Blueprint('audiobooks_route', __name__)

@audiobooks.route('/', methods=['GET'])
def get_all():
    print('getting all audio books')
    audiobooks = dao.get_all()
    return jsonify([book.json() for book in audiobooks])

@audiobooks.route('/id', methods=['GET'])
def get_by_id():
    print (request.args)
    return 'Got request with {}'.format(request.args)


@audiobooks.route('/id', methods=['PUT'])
def update_by_id():
    print (request.args)
    return 'PUT request submitted with args: {}'.format(request.args)


