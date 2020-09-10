# a Dockerfile must begin with FROM, which specifies the parent image
FROM python:3

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY example_image.py .

VOLUME /code

CMD ["python", "./example_image.py"]