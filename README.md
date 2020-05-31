[![codecov](https://codecov.io/gh/dansterenson/Noesis/branch/master/graph/badge.svg)](https://codecov.io/gh/dansterenson/Noesis)
[![Build Status](https://travis-ci.org/dansterenson/Noesis.svg?branch=master)](https://travis-ci.org/dansterenson/Noesis)

# Noesis
Noesis is project that supports a Brain Computer Interface — imaginary hardware that can read minds, and upload snapshots of cognitions.
The project includes a client, which streams cognition snapshots to a server, which then publishes them to a message queue, where multiple parsers read the snapshot, parse various parts of it, and publish the parsed results, which are then saved to a database.
The results are then exposed via a RESTful API, which is consumed by a CLI; there's also a GUI, which visualizes the results in various ways.

<p align="center">
<img src="https://github.com/dansterenson/Brain-Computer-Interface/blob/master/images/project%20desc.png?raw=true )" width="550" />
</p>



## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:dansterenson/Noesis.git
    ...
    $ cd Noesis/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [Noesis] $ # you're good to go!
    ```

3. To check that everything is working as expected, run the tests:


    ```sh
    $ pytest tests/
    ...
    ```
## Deployment

To run all of the services together for a quick start using Docker:

   ```sh
    $ .scripts/run-pipeline.sh
   ```
When all services are running, you can access the GUI at http://localhost:8080

## Usage

After installation is completed and all services are running. use the client module to upload user's snapshots to the system 
(Sample file example can be downloaded from 
[here](https://storage.googleapis.com/advanced-system-design/sample.mind.gz))

```sh
    [Noesis] $ python -m Noesis.client upload-sample 
                      path_to_file
                      -h 0.0.0.0 -p 8000 
   ```
After uploading is completed, you can view the results in the GUI:
   ```sh
    [Noesis] $ http://localhost:8080
   ```
Or use the CLI to see the results

<p align="center">
<img src="https://user-images.githubusercontent.com/38375556/83055082-09cbad80-a05c-11ea-85f7-df90b1b8fb6f.gif" width="750"/>
</p>

## Documentation
The full documenation is available [here](https://Noesis.readthedocs.io/en/latest/index.html).


