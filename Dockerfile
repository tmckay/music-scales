FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt  ./ 
RUN pip3 install --requirement requirements.txt

COPY setup.py ./
COPY mypy.ini ./
COPY music_scales music_scales/
RUN pip3 install .
