from flask import Blueprint, request, jsonify
from app.persistence import AudiobookDAO
from app.model import AudioBook
from app.persistence import connection_manager


dao = AudiobookDAO(connection_manager=connection_manager)
api = Blueprint( 'audiobooks', __name__ )

@api.route( '/', methods=[ 'GET' ] )
def get_all():
    audiobooks = dao.get_all()
    return jsonify([book.json() for book in audiobooks])


@api.route( '/', methods=[ 'POST' ] )
def add_audiobook():
    audiobook = AudioBook.from_json(**request.get_json())
    dao.insert(audiobook)
    return jsonify(audiobook.json())


@api.route( '/', methods=[ 'PUT' ] )
def update():
    audiobook = AudioBook.from_json(**request.get_json())
    dao.update(audiobook)
    return jsonify({'message': 'Successfully updated audiobook', 'audiobook': audiobook.json()})


@api.route( '/id/<int:id>', methods=[ 'DELETE' ] )
def delete(id):
    dao.delete(id)
    return jsonify({'message': 'Audiobook with {id} was successfully deleted'.format(id=id)})


@api.route( '/id/<int:id>', methods=[ 'GET' ] )
def get_by_id(id):
    audiobook = dao.get_by_id(id)
    return jsonify(audiobook.json())