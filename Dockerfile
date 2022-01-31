FROM ubuntu:20.04

RUN apt-get update

FROM python 

WORKDIR '/app'

RUN python -m pip install bottle redis  & python -m pip install bs4 & python -m pip install pymongo & python -m pip install jupyter

COPY . .

CMD ["python", "main.py"]

