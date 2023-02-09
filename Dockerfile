FROM python:slim

RUN useradd DMS

WORKDIR /home/DMS

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY DMS.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP DMS.py

RUN chown -R DMS:DMS ./
USER DMS

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
