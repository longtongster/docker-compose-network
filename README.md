# To Do
Bind a directory

## General remarks:
- use the python logging module to show messages when `docker container logs <container id>` is used

## Introduction

This objective of this repository is to show how networking works with docker and docker-compose. 

The repo contains a very simple app that consists of two parts. There is a very simple httpd container which works
standalone. There is also a very simple flask app that has two buttons. Clicking the first button shows a simple text
message that is part of the flask app. Clicking button 2 sends a request to the httpd container using the name of the 
container (or service in docker-compose)

## Method 1 - without docker-compose

Objective:
show that we can call the httpd container by the container name (`httpd_service`) using the custom network.

1. Create a custom network

    `docker network create my-nw`
2. Create httpd image - cd in the httpd directory

    `docker build -t httpd-img .`
3. Run the httpd container

    `docker run -d -p 8080:80 --network my-nw --name httpd_service httpd-img`

    You can test the container `http://localhost:8080`. Please note that you do not need `EXPOSE` in the docker file to expose ports. Of course it makes explicit what ports your container is listening on.
4. Create app image - cd in the app directory

   `docker build -t app .`
5. Run the app container 

    `docker run -d -p 5000:5000 --network my-nw --name app -e HTTPD-HOST=httpd_service app`

#### Remarks:
- in step 3 the port was available on the localhost due to the port mapping. This can be ommited since the communication 
   of te app is via the custom network. So you can replace the code there by:
`docker run -d --network my-nw --name httpd-service httpd-img`

## Method 2 - with docker-compose

Go to main directory and run

`docker-compose up -d`

To stop the services type 

`docker-compose down` 

docker-compose will automatically remove the containers


