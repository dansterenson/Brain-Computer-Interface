import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import datetime as dt
from website import Website

_INDEX_HTML = '''
<html>
    <head></head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
'''
_USER_LINE_HTML = '''
<li><a href="/users/{user_id}">user {user_id}</a></li>
'''

_THOUGHT = '''
    <tr>
        <td>{time}</td>
        <td>{thought}</td>
    </tr>
'''

_INDEX_USER = '''
<html>
    <head>
        <title>Brain Computer Interface: User {user_id}</title>
    </head>
    <body>
        <table>
            {thoughts}
        </table>
    </body>
</html>
'''


def run_webserver(address, data_dir):
    website = Website()

    @website.route('/')
    def index():
        users_html = []
        html_path = Path(data_dir)
        for user_dir in html_path.iterdir():
            users_html.append(_USER_LINE_HTML.format(user_id=user_dir.name))
        return 200, _INDEX_HTML.format(users='\n'.join(users_html))

    @website.route('/users/([0-9]+)')
    def user(user_id):
        users_html = []
        html_path = Path(data_dir) / str(user_id)
        for file in html_path.iterdir():
            with open(f"{file}", "r") as f:
                time_of_thought1 = file.name.split(".")[0]
                temp_list1 = time_of_thought1.split("-")
                temp_list2 = temp_list1[2].split("_")
                three = temp_list2[0]
                fourth = temp_list2[1]
                datetime = dt.datetime(int(temp_list1[0]), int(temp_list1[1]),
                                       int(three), int(fourth),
                                       int(temp_list1[3]), int(temp_list1[4]))
                users_html.append(_THOUGHT.format(time=datetime, thought=f.read()))
        return 200, _INDEX_USER.format(thoughts='\n'.join(users_html), user_id=user_id)

    website.run(address)


def main(argv):
    if len(argv) < 2 or type(argv[1]) is not str or type(argv[2]) is not str:
        print("Error: arguments not in the right format")
        return 1
    address = argv[1].split(":")
    port = int(address[1])
    run_webserver((address[0], port,), argv[2])


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
