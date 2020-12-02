FROM python:3.6-slim

WORKDIR /usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
    vim \
    python \
    python-pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","./up.py"]