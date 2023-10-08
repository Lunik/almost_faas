# Simple function

This is the simple hello world function. It is used to demonstrate the basic functionality of the framework.

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
