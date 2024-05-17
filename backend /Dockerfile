FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

CMD ["python3","manage.py","runserver"]