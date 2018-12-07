FROM python:3.6.5-slim-jessie

RUN groupadd  django \
    && useradd -g django django

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements
ARG DB_HOST
ARG DB_USER
ARG DB_PASS
ARG DB_PORT

ENV PYTHONUNBUFFERED 1
ENV DB_HOST ${DB_HOST}
ENV DB_USER ${DB_USER}
ENV DB_PASS ${DB_PASS}
ENV DB_PORT ${DB_PORT}

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