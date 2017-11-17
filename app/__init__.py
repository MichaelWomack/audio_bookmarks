from flask import Flask, send_file

app = Flask(__name__, 
    static_folder='../ui/dist', 
    static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)