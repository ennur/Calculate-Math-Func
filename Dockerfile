FROM python:3.9.0-alpine

WORKDIR /case-study

ADD . /case-study

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["main.py"]
