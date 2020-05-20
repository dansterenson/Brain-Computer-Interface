FROM python:3.8.2-alpine3.11

COPY api /Noesis/Noesis/api
COPY data_base /Noesis/Noesis/data_base
RUN mv /Noesis/Noesis/api/requirements.txt /Noesis/Noesis

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt

CMD ["python3", "-m", "Noesis.api", "run-server"]