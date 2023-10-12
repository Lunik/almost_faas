# Author: Lunik
# LICENCE: GPLv3

ARG FUNCTION_VERSION

FROM function/python:${FUNCTION_VERSION}

COPY ./function.py /functions

ENV FUNCTION_HANDLER="function:bp"