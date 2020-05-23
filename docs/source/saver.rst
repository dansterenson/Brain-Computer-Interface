Saver Package
=============

API & CLI
^^^^^^^^^

The saver should be available as Noesis.saver and expose the following API:

    >>> from Noesis.saver import Saver
    >>> saver = Saver(database_url)
    >>> data = …
    >>> saver.save('pose', data)

Which connects to a database, accepts a topic name and some data, as consumed from the message queue, and saves it to the database. It should also provide the following CLI:

And the following CLI:

.. code-block:: bash

    $ python -m Noesis.saver save                     \
      -d/--database 'mongodb://localhost:27017' \
     'pose'                                       \
     'pose.result'

Which accepts a topic name and a path to some raw data, as consumed from the message queue, and saves it to a database.

The CLI should also support running the saver as a service, which works with a message queue indefinitely; it is then the saver's responsibility to subscribe to all the relevant topics it is capable of consuming and saving to the database.

.. code-block:: bash

    $ python -m Noesis.saver run-saver  \
      'mongodb://localhost:27017' \
      'rabbitmq://127.0.0.1:5672/'

