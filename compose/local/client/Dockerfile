FROM node:8.10.0-alpine

RUN apk update && apk upgrade && apk add git

#ADD ./client /usr/src/app/
RUN npm install

COPY ./compose/local/client/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

#RUN npm run build
#RUN npm run generate
#ENV HOST 0.0.0.0
#EXPOSE 3000
#
#CMD [ "npm", "start" ]
