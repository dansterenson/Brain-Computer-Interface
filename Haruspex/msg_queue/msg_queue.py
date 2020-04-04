from urllib.parse import urlparse
from .rabbitMQ import RabbitMQ

supported_mq = {'rabbitmq': RabbitMQ}


def get_mq(url):
    parsed_url = urlparse(url)
    for scheme in supported_mq.keys():
        if parsed_url.scheme == scheme:
            found_mq = supported_mq[scheme]
            return found_mq(parsed_url.host, parsed_url.port)
    raise ValueError(f'url is invalid: {url}')


class MessageQueue:
    def __init__(self, url):
        self.msg_queue = get_mq(url)

    def exchange_declaration(self, name):
        self.msg_queue.exchange_declaration(name)

    def queue_declaration(self, name):
        self.msg_queue.queue_declaration(name)

    def queue_publish(self, name, routing_key, message_to_publish):
        self.msg_queue.queue_publish(name, routing_key, message_to_publish)

    def queue_binding(self, queue_name, exchange_name):
        self.msg_queue.queue_binding(queue_name, exchange_name)

    def consume_from_queue(self, queue_name, callback):
        self.msg_queue.consume_from_queue(queue_name, callback)

    def close(self):
        self.msg_queue.close()

