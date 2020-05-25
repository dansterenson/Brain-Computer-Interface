FROM node:10-alpine as builder

COPY gui/my-gui /Noesis/Noesis/gui/my-gui
RUN rm -rf /Noesis/Noesis/gui/my-gui/build

RUN cd Noesis/Noesis/gui/my-gui

RUN npm install express --save && mkdir /react-ui && mv node_modules /react-ui

WORKDIR /react-ui
RUN cp -rf /Noesis/Noesis/gui/my-gui/* .
RUN yarn
#RUN yarn build


CMD tail -f /dev/null

#FROM nginx:alpine
#
#
#COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf
#
### Remove default nginx index page
#RUN rm -rf /usr/share/nginx/html/*
#
## Copy from the stahg 1
#COPY --from=builder /react-ui/build /usr/share/nginx/html
#
#EXPOSE 3000 80
#
#ENTRYPOINT ["nginx", "-g", "daemon off;"]
#

#COPY api /Noesis/Noesis/api
#COPY data_base /Noesis/Noesis/data_base
#RUN mv /Noesis/Noesis/api/requirements.txt /Noesis/Noesis
#
#WORKDIR /Noesis
#
#RUN mkdir log_files
#RUN pip install --no-cache-dir -r Noesis/requirements.txt
#
#ENTRYPOINT python3 -m Noesis.api run-server -h '0.0.0.0' -p 5000 --database mongodb://mongodb.containersnetwork:27017