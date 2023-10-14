# Flask function

This repository contains the core router for Python functions (FaaS). The framework is based on Flask and is designed to be used with containers.

## Building the base image

```bash
task build
```

This will create base image with the name `function/python`. The tag version has the following format: `<image_version>-<python_version>`. For example, `1.0.0-3.11`.

The list of builded Python versions can be found in the `Taskfile.yml` file.

## Using the base image

You will need to create a new Dockerfile that inherits from the base image. Then you can add your function code and install the dependencies. See [examples](./examples).

Function listen on port `8080` by default. You can change it by setting the `PORT` environment variable.

Function name is `handler` located in the `function.py` file by default. You can change it by setting the `FUNCTION_HANDLER` environment variable. The format is `<module_name>:<function_name>`.

Function list on path `/` by default. You can change it by setting the `FUNCTION_PATH` environment variable.

Function listen to method `GET` and `POST` by default. You can change it by setting the `FUNCTION_METHODS` environment variable (Comma separated list).

Function listen on `/healthz` path for health check.

## Running the function

First, you need to build the image. See [examples](./examples) if you don't know where to start.

With Docker

```bash
docker run -p 8080:8080 --rm <image_name>
```

With Kubernetes

```bash
kubectl run <pod_name> --image=<image_name> --port=8080
kubectl port-forward <pod_name> 8080:8080
```

### Testing the function

```bash
curl -X POST http://localhost:8080/
```

## Development

This project uses [Taskfile](https://taskfile.dev) to automate the development process. You can find the list of available commands in the `Taskfile.yml` file.

Source code is located in the `app` directory. There are also Python requirements in the `requirements.txt` file. The `scripts` folder holds runtime script like the image `entrypoint`. Finally, the `Dockerfile` is used to build the base image.

The webserver used is [Gunicorn](https://gunicorn.org/).

The base application framework is [Flask](https://flask.palletsprojects.com).