FROM python:3.7.4

WORKDIR /usr/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG  1
ENV SECRET_KEY  foo
ENV DJANGO_ALLOWED_HOSTS localhost 0.0.0.0 127.0.0.1 [::1]

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        musl-dev python3-dev build-essential python-dev

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/
RUN pip3 install -r requirements.txt

COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "localhost:8000"]
