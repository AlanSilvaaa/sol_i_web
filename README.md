# sol_i_web
![python check](https://github.com/AlanSilvaaa/sol_i_web/actions/workflows/pythons_tests.yml/badge.svg)
![linter check](https://github.com/AlanSilvaaa/sol_i_web/actions/workflows/linter.yml/badge.svg)
![docker check](https://github.com/AlanSilvaaa/sol_i_web/actions/workflows/docker_push.yml/badge.svg)

Python app that returns the current time using fastAPI

## Running the app

### Docker way
This project is dockerized. You can run it using Docker. Make sure you have Docker installed and running on your machine.

You can run it by building the image and then running the container, or you can pull the image from Docker Hub and run it directly.
#### By pull
Make sure that you got configured you SSH key in your linux system  
```bash
docker pull teg57/sol_i_web
```
```bash
docker run --rm -p 8000:8000 sol_i_web
```
#### By build
Clone the repository to your local machine and then build the image using the following command:  
```bash
docker build -t sol_i_web .
```

### Run
```bash
docker run --rm -p 8000:8000 sol_i_web
```

### Uvicorn way
Make sure that you have a python version equal or above 3.12
Clone the repository:  
```bash
git clone https://github.com/AlanSilvaaa/sol_i_web.git
```
Run the next command to install poetry:  
```bash
pip install poetry
```
Run this command to create poetry enviroment:
```bash
poetry install --no-root
```
Finally run this command to run the source code:
```bash
poetry run uvicorn main:app --port 8000
```
This going to run the local server to display the app, so you have to go to the next endpoint, copy into your favorite browser:
```bash
127.0.0.1:8000/time
```
#### Curl in you want
To visualize the result of the local server you could try to use Curl, run this command:
```bash
curl http://127.0.0.1:8000/time
```
If you local server is running alright, this must return somethin like:  
```bash
{"Date and time": "2025-04-06 12:34:56"}
```

### Docker Hub link
https://hub.docker.com/r/teg57/sol_i_web 
