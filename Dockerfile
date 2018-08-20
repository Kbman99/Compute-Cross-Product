FROM ubuntu:18.04

# -- Install Pipenv:
RUN apt update && apt install python3-pip git -y && pip3 install pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container: RUN set -ex && mkdir /app
WORKDIR /app

# -- Copy over Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# -- Install dependencies:
RUN set -ex
RUN pipenv install --python 3.6 --system --deploy

# Copy over main files
COPY setup.cfg setup.py tests/ app/ .env manage.py /app/

# Listen to port 5000 at runtime
EXPOSE 5000

# Run the flask server @ 0.0.0.0
CMD flask run --host 0.0.0.0
