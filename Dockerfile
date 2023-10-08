# Author: Lunik
# LICENCE: GPLv3

ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN apk add --no-cache --update \
  curl

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
  python3 -m pip install --compile --no-cache-dir -r requirements.txt

ENV FUNCTION_FOLDER=/functions
RUN mkdir -p ${FUNCTION_FOLDER}

COPY ./scripts /scripts
RUN chmod +x /scripts/*

WORKDIR /app
COPY ./app .

HEALTHCHECK --interval=5s --timeout=30s --retries=3 CMD /scripts/healthcheck.sh

ENTRYPOINT ["/scripts/entrypoint.sh"]