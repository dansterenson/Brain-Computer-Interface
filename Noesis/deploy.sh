
sudo docker network create containersnetwork
sudo docker run -d --name mongodb -p 27017:27017 --net containersnetwork mongo


sudo docker build -t api -f api/Dockerfile .

sudo docker container ls -a

sudo docker stop api
sudo docker rm api

sudo docker run -d --name api -p 5000:5000/tcp --net containersnetwork api
