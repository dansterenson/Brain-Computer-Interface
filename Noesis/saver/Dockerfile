FROM python:3.8-slim

COPY Noesis/data_base /Noesis/Noesis/data_base
COPY Noesis/msg_queue /Noesis/Noesis/msg_queue
COPY Noesis/parsers /Noesis/Noesis/parsers
COPY Noesis/saver /Noesis/Noesis/saver

RUN mv /Noesis/Noesis/saver/requirements.txt /Noesis/Noesis

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt

ENTRYPOINT python3 -m Noesis.saver run-saver mongodb://mongodb.containersnetwork:27017 rabbitmq://rab.containersnetwork:5672