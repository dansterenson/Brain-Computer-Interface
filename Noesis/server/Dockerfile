FROM python:3.8-slim

COPY msg_queue /Noesis/Noesis/msg_queue
COPY readers /Noesis/Noesis/readers
COPY server /Noesis/Noesis/server

RUN mv /Noesis/Noesis/server/requirements.txt /Noesis/Noesis

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt

ENTRYPOINT python3 -m Noesis.server run-server -h '0.0.0.0' -p '8000' rabbitmq://rab.containersnetwork:5672/