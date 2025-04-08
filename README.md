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
```bash
docker pull teg57/sol_i_web
```

```bash
docker run --rm -p 8000:8000 sol_i_web
```
#### By build
Clone the repository to your local machine and then build the image using the following commands:  
```bash
docker build -t sol_i_web .
```

```bash
docker run --rm -p 8000:8000 sol_i_web
```

### Run locally
Make sure that you have a python version greater or equal to 3.12. Then:

Clone the repository:
```bash
git clone https://github.com/AlanSilvaaa/sol_i_web.git
```

Run the next command to install poetry:  
```bash
pip install poetry
```

Install depencencies along with a poetry enviroment:
```bash
poetry install --no-root
```

Finally go to `src` folder and run this command to run the source code:
```bash
poetry run uvicorn main:app --port 8000
```

### Test API
There are two ways to test the API, using a browser or using curl.
#### Browser
After the local server is started, go to your browser and type the following URL:
```bash
127.0.0.1:8000/time
```
#### Curl
To visualize the result of the local server you can use Curl:
```bash
curl http://127.0.0.1:8000/time
```
If you local server is running fine, it should return something like:
```bash
{"Date and time": "2025-04-06 12:34:56"}
```

### Docker Hub link
[Here](https://hub.docker.com/r/teg57/sol_i_web) you can find the docker image on Docker Hub.
