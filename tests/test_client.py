import requests
from pytest_httpserver import HTTPServer
from Noesis.client.client import upload_sample


def test_client(httpserver: HTTPServer):
    with HTTPServer(host='127.0.0.1', port=8000) as httpserver:
        httpserver.expect_request("/upload_snapshot").respond_with_data("uploaded data")
        upload_sample(('127.0.0.1', 8000), 'tests/data/test_file.mind.gz')
        assert requests.get(httpserver.url_for("/upload_snapshot")).text == "uploaded data"

