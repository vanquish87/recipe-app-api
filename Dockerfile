FROM python:3.7-alpine3.15
LABEL maintainer='jasmeet'

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# dimaag kharab ho gya yeh debug karte hue
# g++ for uwsgi
RUN apk add --no-cache linux-headers g++ 
# for Pillow
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
# for some other stuff
RUN pip install --upgrade pip

# it will turn to True when running via development mode
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 


ENV PATH="/scripts:/py/bin:$PATH"

USER django-user