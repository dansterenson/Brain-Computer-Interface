Client Package
==============

API & CLI
^^^^^^^^^

The client should read the sample and upload it to the server.

The client is available as Noesis.client and expose the following API:

>>> from Noesis.client import upload_sample
>>> upload_sample(host='127.0.0.1', port=8000, path='sample.mind.gz')
… # upload path to host:port

And the following CLI:

.. code-block:: bash

    $ python -m Noesis.client upload-sample \
        -h/--host '127.0.0.1'                       \
        -p/--port 8000                              \
        'snapshot.mind.gz'
    …

The Sample
^^^^^^^^^^

| The sample's format is a  gzipped binary with a sequence of message sizes (uint32) and messages (of that size), where the first one is a User message, and the rest are Snapshot messages
|
| The user and snapshot messages formats are defined in `this .proto file <https://storage.googleapis.com/advanced-system-design/cortex.proto>`_.
|
| A sample example is available `here <https://storage.googleapis.com/advanced-system-design/sample.mind.gz>`_.
