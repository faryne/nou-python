FROM python:3.11.2

COPY . /project
WORKDIR /project

RUN python -m pip install -r requirements.txt

CMD python -m flask run -p 5000 -h 0.0.0.0