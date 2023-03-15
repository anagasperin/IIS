FROM python:3.9.12

WORKDIR /src

COPY pyproject.toml poetry.lock /tmp/poetry/

ENV POETRY_VERSION=1.0

RUN pip install "poetry==$POETRY_VERSION"

CMD python serve/server.py

EXPOSE 5000

# docker build -t juliekenway/frontend:1.0 .
# docker run -it -d -p 4200:4200 --name IIS_nal1 juliekenway/frontend:1.0
# docker push juliekenway/frontend:1.0