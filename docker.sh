docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
sudo docker run -d -p 5672:5672 rabbitmq
sudo docker run -d -p 27017:27017 --name mongodb mongo
sudo docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 rabbitmq:3-management