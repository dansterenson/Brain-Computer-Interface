sudo docker volume create --name dataVolume1
sudo docker network create containersnetwork
sudo docker run -d --name mongodb -p 27017:27017 --net containersnetwork mongo
sudo docker run -d --name rab -p 5672:5672 --net containersnetwork rabbitmq


sudo docker build -t api -f api/Dockerfile .
sudo docker build -f parsers/Dockerfile -t pose --build-arg PARSER_NAME=pose .
sudo docker build -f parsers/Dockerfile -t color_image --build-arg PARSER_NAME=color_image .
sudo docker build -f parsers/Dockerfile -t depth_image --build-arg PARSER_NAME=depth_image .
sudo docker build -f parsers/Dockerfile -t feelings --build-arg PARSER_NAME=feelings .

sudo docker container ls -a


sudo docker stop api
sudo docker rm api

sudo docker run -d --name api -p 5000:5000/tcp -v DataVolume1:/datavolume1 --net containersnetwork api
sudo docker run -d --name pose_parser --net containersnetwork pose
sudo docker run -d --name feelings_parser --net containersnetwork feelings
sudo docker run -d --name color_image_parser -v DataVolume1:/datavolume1 --net containersnetwork color_image
sudo docker run -d --name depth_image_parser -v DataVolume1:/datavolume1 --net containersnetwork depth_image

