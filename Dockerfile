FROM ubuntu:18.04

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
    vim \
    python \
    python-pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python up.py