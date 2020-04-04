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
        return decorator()


