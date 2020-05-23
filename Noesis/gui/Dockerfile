FROM python:3.8-slim

COPY gui /Noesis/Noesis/gui
RUN mv /Noesis/Noesis/gui/requirements.txt /Noesis/Noesis

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt

ENTRYPOINT python3 -m Noesis.gui run-server -h '0.0.0.0' -p 8080