FROM python:3.11

WORKDIR /docker

COPY requirements.txt /docker/requirements.txt

RUN /usr/local/bin/python3 -m pip install -r /docker/requirements.txt

COPY . /docker

CMD ["/usr/local/bin/python3", "/docker/main.py"]
