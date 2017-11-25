from flask import Blueprint, request, jsonify
from app.persistence.audiobook_dao import AudiobookDAO
from app.model.audiobook import AudioBook
from app.config.app_config import Config

config = Config()
dao = AudiobookDAO(config)
audiobooks = Blueprint('audiobooks_route', __name__)

@audiobooks.route('/', methods=['GET'])
def get_all():
    audiobooks = dao.get_all()
    return jsonify([book.json() for book in audiobooks])


@audiobooks.route('/id/<int:id>', methods=['GET'])
def get_by_id(id):
    audiobook = dao.get_by_id(id)
    return jsonify(audiobook.json())


@audiobooks.route('/id', methods=['PUT'])
def update_by_id(id):
    audiobook = AudioBook.from_json(request.json())
    audiobook = dao.update(audiobook)
    return jsonify(audiobook.json())

