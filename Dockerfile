FROM python:3.7-alpine
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /flaskapp
WORKDIR /flaskapp
ENTRYPOINT ["python"]
CMD ["app.py"]
