import inspect


class AddParser:
    parsers_dict = {}

    @classmethod
    def add_to_parser_list(cls, parser_name):
        def decorator(parser):
            # parser is either a class or a function
            if inspect.isclass(parser):
                cls.parsers_dict[parser_name] = parser.parse
            elif inspect.isfunction(parser):
                cls.parsers_dict[parser_name] = parser
            else:
                raise Exception
            return parser
        return decorator


def run_parser(parser_name, data):
    cur_parser = AddParser.parsers_dict[parser_name]
    if cur_parser is None:
        return f"invalid parser: {parser_name}"
    return cur_parser(data)