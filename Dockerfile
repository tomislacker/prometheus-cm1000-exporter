FROM       python:3.6-alpine
MAINTAINER "tomislacker" <tomislacker@users.noreply.github.com>

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY arrisparser /app/arrisparser
WORKDIR /app

CMD ["python","-m","arrisparser"]
