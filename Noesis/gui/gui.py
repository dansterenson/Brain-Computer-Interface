from flask import Flask, send_from_directory
from flask_cors import CORS
import requests
import os


def run_server(host='127.0.0.1', port=8080, api_host='127.0.0.1', api_port=5000):
    app = Flask(__name__, static_folder='my-gui/build')
    cors = CORS()

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    app.run(use_reloader=True, host=host, port=port, threaded=True)