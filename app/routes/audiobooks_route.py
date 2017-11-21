from flask import Blueprint, request


audiobooks = Blueprint('audiobooks_route', __name__)


@audiobooks.route('/id', methods=['GET'])
def get_by_id():
    print request.args
    return 'Got request with {}'.format(request.args)


@audiobooks.route('/id', methods=['PUT'])
def update_by_id():
    print request.args
    return 'PUT request submitted with args: {}'.format(request.args)
