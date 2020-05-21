FROM python:3.8.2-alpine3.11
ARG PARSER_NAME
COPY parsers /Noesis/Noesis/parsers

COPY msg_queue /Noesis/Noesis/msg_queue
RUN mv /Noesis/Noesis/parsers/requirements.txt /Noesis/Noesis

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt
RUN echo ${PARSER_NAME}

ENTRYPOINT python3 -m Noesis.parsers run-parser ${PARSER_NAME} rabbitmq://rab.containersnetwork:5672