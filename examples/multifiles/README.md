# Multifile function

This is a function that uses multiple files. It is used to demonstrate the basic functionality of the framework.

The function base code is located in the `function.py` file and the image build configuration is in the `Dockerfile` file.

It also uses modules located in the `lib` directory.

## Building the image

```bash
docker build \
  --build-arg FUNCTION_VERSION=latest \
  --tag demo/function/multifile:latest \
  --file Dockerfile \
  .
```

## Running the function

See [README.md](../../README.md) for more information.
