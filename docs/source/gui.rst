GUI Package
===========

API & CLI
^^^^^^^^^

The GUI consumes the API and reflects it

    >>> from cortex.gui import run_server
    >>> run_server(
    ...     host = '127.0.0.1',
    ...     port = 8080,
    ...     api_host = '127.0.0.1',
    ...     api_port = 5000,
    ... )



.. code-block:: bash

    $ python -m cortex.gui run-server \
      -h/--host '127.0.0.1'       \
      -p/--port 8080              \
      -H/--api-host '127.0.0.1'   \
      -P/--api-port 5000
