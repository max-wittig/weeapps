FROM node:13

WORKDIR /opt/weeapps/

COPY . .

RUN yarn

EXPOSE 8080

ENTRYPOINT ["yarn"]
CMD ["serve", "--mode", "prod", "--host", "0.0.0.0"]
