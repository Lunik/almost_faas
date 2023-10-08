# Simple function

This is the simple function that return a custom response. It is used to demonstrate how to return a custom response from a function.

The function code is located in the `function.py` file and the image build configuration is in the `Dockerfile` file.

## Building the image

```bash
docker build \
  --build-arg FUNCTION_VERSION=latest \
  --tag demo/function/simple:latest \
  --file Dockerfile \
  .
```

## Running the function

See [README.md](../../README.md) for more information.
