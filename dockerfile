FROM python:3.7.4
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
