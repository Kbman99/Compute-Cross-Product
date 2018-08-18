# Dockerfile for dev
FROM node:latest

WORKDIR /client
COPY . /client

RUN npm install --no-progress --ignore-optional

EXPOSE 8080

CMD npm run start-docker