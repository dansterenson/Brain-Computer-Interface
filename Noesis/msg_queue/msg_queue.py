from urllib.parse import urlparse
import pkgutil
from os.path import dirname
from importlib import import_module


class MessageQueue:
    def __init__(self, url):
        self.supported_mq = {}
        self.load_all_mq()
        self.mq_queue_type = self.get_mq(url)

    def exchange_declaration(self, name):
        self.mq_queue_type.exchange_declaration(name)

    def queue_declaration(self, name):
        return self.mq_queue_type.queue_declaration(name)

    def queue_publish(self, name, routing_key, message_to_publish):
        self.mq_queue_type.queue_publish(name, routing_key, message_to_publish)

    def queue_binding(self, queue_name, exchange_name):
        self.mq_queue_type.queue_binding(queue_name, exchange_name)

    def consume_from_queue(self, queue_name, callback):
        self.mq_queue_type.consume_from_queue(queue_name, callback)

    def start_consuming(self):
        self.mq_queue_type.start_consuming()

    def close(self):
        self.mq_queue_type.close()

    def load_all_mq(self):
        pwd = dirname(__file__)
        for (_, name, _) in pkgutil.iter_modules([pwd]):
            if name.endswith('mq'):
                module = import_module('Noesis.msg_queue' + '.' + name)
                for name_attr in dir(module):
                    if name_attr.endswith("MQ"):
                        self.supported_mq[name] = getattr(module, name_attr)

    def get_mq(self, url):
        parsed_url = urlparse(url)
        for scheme in self.supported_mq.keys():
            if parsed_url.scheme == scheme:
                found_mq = self.supported_mq[scheme]
                host = parsed_url._hostinfo[0]
                port = parsed_url._hostinfo[1]
                return found_mq(host, int(port))
        raise ValueError(f'url is invalid: {url}')
