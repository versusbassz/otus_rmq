FROM rabbitmq:3.13.1-management-alpine

RUN apk add --update python3 py3-requests
