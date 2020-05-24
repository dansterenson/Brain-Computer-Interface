FROM node:10-alpine as builder

COPY gui Noesis/Noesis/gui/my-gui

RUN cd Noesis/Noesis/gui/my-gui

RUN npm install express --save && mkdir /react-ui && mv node_modules /react-ui

WORKDIR /react-ui

RUN cp -r /Noesis/Noesis/gui/my-gui/*  /react-ui
RUN npm rebuild node-sass
RUN yarn build
CMD tail -f /dev/null

#FROM python:3.8-slim
#
#WORKDIR /Noesis
#RUN rsync -av --progress Noesis/gui /react-ui --exclude my-gui
#
#RUN mv /Noesis/Noesis/api/requirements.txt /react-ui
#
#WORKDIR /Noesis
#
#RUN mkdir log_files
#RUN pip install --no-cache-dir -r Noesis/requirements.txt
#
#ENTRYPOINT python3 -m Noesis.api run-server -h '0.0.0.0' -p 5000 --database mongodb://mongodb.containersnetwork:27017
#