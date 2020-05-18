from flask import Flask, render_template, jsonify,make_response
from flask_cors import CORS
import requests


def run_server(host='127.0.0.1', port=8080, api_host='127.0.0.1', api_port=5000):
    app = Flask(__name__, static_folder='./my-gui/build/static',  template_folder="./my-gui/build")
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    @app.route('/api/<path:path>')
    def api_call(path):
        if (path.endswith('data')):
            return make_response(jsonify(f'http://{api_host if api_host != "api" else "localhost"}:{api_port}/{path}'),
                                 200)
        return make_response(jsonify(requests.get(f'http://{api_host}:{api_port}/{path}').json()), 200)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template('index.html')

    app.run(host=host, port=port)
