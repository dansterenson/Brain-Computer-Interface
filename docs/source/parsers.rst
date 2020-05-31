Parsers Package
===============

API & CLI
^^^^^^^^^

The parsers are simple functions, built on top of a platform, and easily deployable as microservices consuming raw data from the queue, and producing parsed results to it

The parsers ar available as Noesis.parsers and expose the following API:

    >>> from Noesis.parsers import run_parser
    >>> data = …
    >>> result = run_parser('pose', data)

Which accepts a parser name and some raw data, as consumed from the message queue, and returns the result, as published to the message queue.

And the following CLI:

.. code-block:: bash

    $ python -m Noesis.parsers parse 'pose' 'snapshot.raw' > 'pose.result'

Which accepts a parser name and a path to some raw data, as consumed from the message queue, and prints the result, as published to the message queue (optionally redirecting it to a file).

The CLI should also support running the parser as a service, which works with a message queue indefinitely.

.. code-block:: bash

    $ python -m Noesis.parsers run-parser 'pose' 'rabbitmq://127.0.0.1:5672/'

Implemented Parsers
^^^^^^^^^^^^^^^^^^^
**Pose**
    | Collects the translation and the rotation of the user's head at a given timestamp, and publishes the result to a dedicated topic.

**Color Image**
    | Collects the color image of what the user was seeing at a given timestamp, and publishes the result to a dedicated topic.
    | **Note**: the data itself should be stored to disk, and only the metadata published.

**Depth Image**
    | Collects the depth image of what the user was seeing at a given timestamp, and publishes the result to a dedicated topic.
    | A depth image is a width × height array of floats, where each float represents how far the nearest surface from the user was, in meters. So, if the user was looking at a chair, the depth of its outline would be its proximity to her (for example, 0.5 for half a meter), and the wall behind it would be farther (for example, 1.0 for one meter).
    | **Note**: the data itself should be stored to disk, and only the metadata published.

**Feelings**
Collects the feelings the user was experiencing at any timestamp, and publishes the result to a dedicated topic.


How To Add New Parsers
^^^^^^^^^^^^^^^^^^^^^^

#. Create a new python file in Noesis.parsers with a name of '*parser_<parser_name_goes_here>.py*'.
#. Inside the new file, add a function (can be in a class) named "parse" as follows:
#. Return a json format of the user's info, timestamp, parser's name and the parsed data.
#. Implement the parse method as follows:

 .. code-block:: python

       def parse(data):
           metadata = get_metadata(data)
           #
           # parse data
           #
           return {'user_info': user_info,
            'timestamp': data['timestamp'],
            'result_name': <parser_name>,
            'data': <parsed_data>
