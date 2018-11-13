FROM node:10-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN apk update && apk upgrade \
    && apk add --no-cache git g++ ca-certificates bash

# - to keep it clean and small, run 'npm cache clean --force' after above
RUN npm install #&& npm cache clean --force

# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

EXPOSE 3000
CMD [ "npm", "run", "start" ]
