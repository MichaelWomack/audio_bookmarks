from flask import Blueprint, jsonify, request
from gutils.gcp.storage import CloudStorage

from app import config
from app.model import AudioBook
from app.persistence import AudiobookDAO, connection_manager

cloud_storage = CloudStorage.with_default_credentials()
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


@api.route('/upload/id/<int:id>', methods=['POST'])
def upload(id):
    if 'file' in request.files:
        f = request.files[ 'file' ]
        audiobook = dao.get_by_id(id)

        if not audiobook:
            return jsonify(dict(message='Audiobook with id {id} does not exist.'.format(id=id))), 400

        blob = cloud_storage.upload_blob_from_file(config.storage_bucket, f.name, f)
        audiobook.storage_url = blob.media_link
        dao.update(audiobook)
        return jsonify(dict(message=dir(blob)))
    else:
        return jsonify(dict(message='No multipart form data containing \'file\' was uploaded')), 400