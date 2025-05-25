FROM docker.io/python:3.13.3-alpine

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN rm requirements.txt

WORKDIR /api

COPY . .

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000" ]