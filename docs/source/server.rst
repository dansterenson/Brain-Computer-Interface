Server Package
==============

API & CLI
^^^^^^^^^

The server should accept connection, receive the uploaded samples and publish them to its message queue.

The server is available as Noesis.servers and expose the following API:

>>> from Noesis.server import run_server
>>> def print_message(message):
...     print(message)
>>> run_server(host='127.0.0.1', port=8000, publish=print_message)
… # listen on host:port and pass received messages to publish

And the following CLI:

.. code-block:: bash

    $ python -m Noesis.server run-server \
      -h/--host '127.0.0.1'          \
      -p/--port 8000                 \
      'rabbitmq://127.0.0.1:5672/'
