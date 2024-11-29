ARG PYTHON_VERSION=3.11-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /mbti

WORKDIR /mbti

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY mbti/manage.py /mbti/
COPY mbti /mbti


ENV SECRET_KEY "gRqqzb7lIYPkRwLK25AOFiIze48eN26jICS5RxKXq2stEpaayz"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn","--bind",":8000","--workers","2","mbti.wsgi"]
