#let's attempt to use volumes for whole project. for example of built project look at polls
FROM python:3.9.6-slim
#FROM debian:buster-20210721-slim

ENV PYTHONUNBUFFERED 1 

#don't need these for using volume for live code development
#will need this when dockerizing app for deployment

#RUN mkdir /code
#don't need to copy contents since we are using volumes to edit live
#COPY . /code
#WORKDIR /code

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

#RUN apt update \ 
#	&& apt install -y python3-dev default-libmysqlclient-dev build-essential python3-pip \ 
#	&& pip3 install --no-cache-dir -r requirements.txt \
#	&& apt-get purge -y  



