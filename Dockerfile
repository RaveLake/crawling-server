FROM tiangolo/uwsgi-nginx-flask:python3.9

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./config/requirements.txt /tmp/custom_requirements.txt
RUN pip install -r /tmp/custom_requirements.txt

# language
RUN apt-get clean && apt-get update && apt-get install -y locales && locale-gen ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8

# TimeZone
ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /app/log
COPY config/nginx.flask.conf /etc/nginx/conf.d/flask.conf
COPY config/uwsgi.ini /app/uwsgi.ini
COPY ./app.py /app/main.py
COPY ./src/ /app/src/

ARG FLASK_DATABASE_URI
ENV DATABASE_URI $FLASK_DATABASE_URI
ENV LOCALHOST host.docker.internal
ENV LISTEN_PORT 8080
EXPOSE 8080
