\# DevOps API Project



\## Overview

This project is a simple REST API built using Flask and containerized using Docker. It demonstrates core DevOps practices including containerization and CI/CD automation using GitHub Actions.



\---



\## Features

\- REST API with multiple endpoints

\- Docker containerization

\- CI/CD pipeline using GitHub Actions

\- Supports both GET and POST requests for testing



\---



\## Endpoints



\### 1. Health Check

GET /

Response:

API Running



\---



\### 2. Add Numbers

POST /add



Request:

{

&#x20; "a": 5,

&#x20; "b": 3

}



Response:

{

&#x20; "result": 8

}



\---



\### 3. Multiply Numbers



\#### GET (browser-friendly)

GET /multiply?a=4\&b=5



Response:

{

&#x20; "result": 20

}



\#### POST

POST /multiply



Request:

{

&#x20; "a": 4,

&#x20; "b": 5

}



Response:

{

&#x20; "result": 20

}



\---



\## How to Run



\### Run Locally

```bash

pip install flask

python app.py# DevOps API Project



\## Overview

This project is a simple REST API built using Flask and containerized using Docker. It demonstrates core DevOps practices including containerization and CI/CD automation using GitHub Actions.



\---



\## Features

\- REST API with multiple endpoints

\- Docker containerization

\- CI/CD pipeline using GitHub Actions

\- Supports both GET and POST requests for testing



\---



\## Endpoints



\### 1. Health Check

GET /

Response:

API Running



\---



\### 2. Add Numbers

POST /add



Request:

{

&#x20; "a": 5,

&#x20; "b": 3

}



Response:

{

&#x20; "result": 8

}



\---



\### 3. Multiply Numbers



\#### GET (browser-friendly)

GET /multiply?a=4\&b=5



Response:

{

&#x20; "result": 20

}



\#### POST

POST /multiply



Request:

{

&#x20; "a": 4,

&#x20; "b": 5

}



Response:

{

&#x20; "result": 20

}



\---



\## How to Run



\### Run Locally

```bash

pip install flask

python app.py







\### Run using Docker 

docker build -t devops-api .

docker run -p 5000:5000 devops-api





