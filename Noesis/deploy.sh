
sudo docker network create containersnetwork
sudo docker run -d --name mongodb -p 27017:27017 --net containersnetwork mongo


sudo docker build -t api -f api/Dockerfile .
#sudo docker build -f parsers/Dockerfile -t pose --build-arg PARSER_NAME=pose .
#sudo docker build -f parsers/Dockerfile -t color_image --build-arg PARSER_NAME=color_image .
#sudo docker build -f parsers/Dockerfile -t depth_image --build-arg PARSER_NAME=depth_image .
#sudo docker build -f parsers/Dockerfile -t feelings --build-arg PARSER_NAME=feelings .

sudo docker container ls -a

sudo docker stop api
sudo docker rm api

sudo docker run -d --name api -p 5000:5000/tcp --net containersnetwork api

