from flask import Flask
from app.routes.audiobooks_route import audiobooks

app = Flask(__name__, 
    static_folder='../client/dist',
    static_url_path='')

app.register_blueprint(audiobooks, url_prefix='/api/audiobooks')

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
