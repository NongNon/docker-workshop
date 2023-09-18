#__Task-1: find the base image for nodejs 
FROM node:current-alpine

ENV APP_PORT=5000
WORKDIR /app
COPY package.json /app
RUN npm install
# __Task-2: Set Expose port
COPY . /app

# __Task-3: Set Expose port
EXPOSE 5000
CMD ["npm", "start"]
