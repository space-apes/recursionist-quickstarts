FROM node:16.9.1-bullseye-slim


RUN mkdir /app
COPY * /app/
WORKDIR /app


RUN 	apt update \ 
	&& apt upgrade -y  \ 
	&& apt install git -y \
	&& apt-get purge -y \
	&& npm install -g npm \ 
	&& npm install -g typescript --save-dev \ 
	&& npm install -g @angular/cli



