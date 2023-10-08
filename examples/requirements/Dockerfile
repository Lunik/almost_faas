# Author: Lunik
# LICENCE: GPLv3

ARG FUNCTION_VERSION

FROM function/python:${FUNCTION_VERSION}

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
  python3 -m pip install --user --compile --no-cache-dir -r requirements.txt

COPY ./function.py /functions
