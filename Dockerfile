# base image
FROM python:3-alpine 

WORKDIR /zone

RUN apk add --no-cache git && \
    pip install git+https://github.com/KhaingNaing/cpbyext.git#egg=cpbyext && \
    apk del git 

ENTRYPOINT [ "cpbyext" ]
