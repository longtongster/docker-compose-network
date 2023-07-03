# To Do
Bind a directory

## Introduction

In this example two very simple apps are created, a simple flask app and a simple httpd app. The flask app will call
the httpd server over a custom network.

## Method 1 - without docker-compose

Objective:
show that we can call the httpd container by the name using the custom network.

1. Create a custom network

    `docker network create my-nw`
2. Create httpd image - cd in the httpd directory

    `docker build -t httpd-img .`
3. Run the httpd container

    `docker run -d -p 8080:80 --network my-nw --name httpd-service httpd-img`

    You can test the container `http://localhost:8080`
4. Create app image - cd in the app directory

   `docker build -t app .`
5. Run the app container 

    `docker run -d -p 5000:5000 --network my-nw --name app app`

## Method 2 - with docker-compose

Go to main directory and run

`docker-compose up -d`


