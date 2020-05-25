FROM node:10-alpine as builder

COPY gui/my-gui /Noesis/Noesis/gui/my-gui
RUN rm -rf /Noesis/Noesis/gui/my-gui/build

RUN cd Noesis/Noesis/gui/my-gui

RUN npm install express --save && mkdir /react-ui && mv node_modules /react-ui

WORKDIR /react-ui
RUN cp -rf /Noesis/Noesis/gui/my-gui/* .

RUN yarn
RUN yarn build

FROM python:3.8-slim

COPY gui /Noesis/Noesis/gui
RUN rm -rf /Noesis/Noesis/gui/my-gui

RUN mv /Noesis/Noesis/gui/requirements.txt /Noesis/Noesis

COPY --from=builder /react-ui/build /Noesis/Noesis/gui/my-gui/build

WORKDIR /Noesis

RUN mkdir log_files
RUN pip install --no-cache-dir -r Noesis/requirements.txt

ENTRYPOINT python3 -m Noesis.gui run-server -h '0.0.0.0' -H 'api'
EXPOSE 8080
