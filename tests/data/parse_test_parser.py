from .parser_manager import user_info_data


def parse(data):
    user_info = user_info_data(data)
    return {'user_info': user_info,
            'timestamp': data['timestamp'],
            'result_name': 'test_parser',
            'data': {"testing_adding_parser"}}