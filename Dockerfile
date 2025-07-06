FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

# Run unit tests at build time
RUN python -m unittest discover -s tests

CMD ["python"]
