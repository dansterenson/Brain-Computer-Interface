docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker volume rm $(docker volume ls -f dangling=true -q)
#sudo docker run -d -p 5672:5672 rabbitmq
#sudo docker rmi $(docker images -f dangling=true -q)
#sudo docker run -d -p 27017:27017 --name mongodb mongo
