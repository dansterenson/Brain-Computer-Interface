import click
import pathlib
from .add_parser import AddParser
from ..msg_queue import MessageQueue
@click.group()
def cli():
    pass


@cli.command('parse')
@click.argument('parser_name')
@click.argument('path_to_data')
def parse_cmd(parser_name, path_to_data):
    #if not path.is_file(): TODO
    #    print(f'Path is invalid.')
    #    return 1
    cur_parser = AddParser.parsers_dict[parser_name]
    if cur_parser is None:
        return f'parser name: {parser_name} is invalid'

    with open(path_to_data, 'r') as file_to_read:
        data = file_to_read.read()
        parsed_data = cur_parser(data)
        print(parsed_data)

@cli.command('run-parser')
@click.argument('parser_name')
@click.argument('message_queue_url')
def run_parser_cmd(parser_name, message_queue_url): #TODO
    cur_parser = AddParser.parsers_dict[parser_name]
    if cur_parser is None:
        return f'parser name: {parser_name} is invalid'
    message_queue = MessageQueue(message_queue_url)
    message_queue.exchange_declaration("snapshots")
    message_queue.queue_declaration(parser_name)
    message_queue.queue_binding(parser_name, 'snapshots')


if __name__ == '__main__':
    cli()
