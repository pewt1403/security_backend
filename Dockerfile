FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements ./requirements
RUN pip install -r ./requirements/local.txt
COPY . .
CMD ["bash", "-c", "while !</dev/tcp/database/5432; do sleep 1; done; python manage.py migrate --database production; python manage.py runserver 0.0.0.0:8000"]