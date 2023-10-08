# Parameters function

This is the function that takes parameters and returns them in the response. It is used to demonstrate how to pass parameters to a function.

The function code is located in the `function.py` file and the image build configuration is in the `Dockerfile` file.

## Building the image

```bash
docker build \
  --build-arg FUNCTION_VERSION=latest \
  --tag demo/function/parameters:latest \
  --file Dockerfile \
  .
```

## Running the function

See [README.md](../../README.md) for more information.
