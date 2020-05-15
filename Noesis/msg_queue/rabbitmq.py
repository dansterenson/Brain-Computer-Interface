import pika


class RabbitMQ:
    def __init__(self, host, port):
        parameters = pika.ConnectionParameters(host, port)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def exchange_declaration(self, name):
        self.channel.exchange_declare(exchange=name, exchange_type='fanout')

    def queue_declaration(self, name):
        return self.channel.queue_declare(queue=name, exclusive=True)

    def queue_publish(self, name, routing_key, message_to_publish):
        self.channel.basic_publish(exchange=name, routing_key=routing_key, body=message_to_publish)

    def queue_binding(self, queue_name, exchange_name):
        self.channel.queue_bind(exchange=exchange_name, queue=queue_name)

    def consume_from_queue(self, queue_name, callback):
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    def start_consuming(self):
        self.channel.start_consuming()

    def close(self):
        self.channel.close()




