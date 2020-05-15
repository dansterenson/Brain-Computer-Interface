from .parser_manager import user_info_data


def parse(data):
    user_info = user_info_data(data)
    return {'user_info': user_info,
            'timestamp': data['timestamp'],
            'result_name': 'feelings',
            'data': {'hunger': data['feelings'][0],
                     'thirst': data['feelings'][1],
                     'exhaustion': data['feelings'][2],
                     'happiness': data['feelings'][3]}}