FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements ./requirements
RUN pip install -r ./requirements/local.txt
COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
CMD /wait && python manage.py migrate && gunicorn --access-logfile - --workers 4 --bind 0.0.0.0:8000 security_backend.wsgi:application