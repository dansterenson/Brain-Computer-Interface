from . import parsers_dict




#class ParserMng:
#
#    @classmethod
#    def load_parsers_modules(cls):
#        #pwd = dirname(__file__)
#        #for (_, name, _) in pkgutil.iter_modules([pwd]):
#        #    if name.startswith('parse_'):
#        #        import_module('parsers' + '.' + name)
#        cur_module = pathlib.Path(__file__)
#        root = cur_module.parent
#        for path in root.iterdir():
#            if path.name == cur_module.name:
#                continue
#            if path.name.startswith('parse_'):
#                package = f'{root.parent.name}.{root.name}'
#                import_module(f'.{path.stem}', package=package)


def run_parser(parser_name, data):
    cur_parser = parsers_dict[parser_name]
    if cur_parser is None:
        return f"invalid parser: {parser_name}"
    return cur_parser(data)