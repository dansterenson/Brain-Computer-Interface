FROM python:3.8-slim
ARG PARSER_NAME
COPY parsers /Noesis/Noesis/parsers

COPY msg_queue /Noesis/Noesis/msg_queue
RUN mv /Noesis/Noesis/parsers/requirements.txt /Noesis/Noesis
ARG PARSER_NAME
ENV PARSER_ENV_NAME=${PARSER_NAME}

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt
RUN echo ${PARSER_NAME}

ENTRYPOINT python3 -m Noesis.parsers run-parser ${PARSER_ENV_NAME} 'rabbitmq://rab.containersnetwork:5672/'
