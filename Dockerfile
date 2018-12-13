FROM python:3.6.5-slim-jessie

RUN groupadd  django \
    && useradd -g django django

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements

ENV PYTHONUNBUFFERED 1

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN sed -i 's/\r//' /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
RUN chown django /docker-entrypoint.sh

COPY . /ssbbs_backend
RUN chown -R django /ssbbs_backend
USER django
WORKDIR /ssbbs_backend
EXPOSE 5000
ENTRYPOINT ["/docker-entrypoint.sh"]