FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pipenv


COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY . .

EXPOSE 8084

CMD ["pipenv", "run", "python", "asgi.py"]