#!/bin/sh
# Run from within ./app directory
USERNAME=organization-name
IMAGE=tennapp

docker build -t ${USERNAME}/${IMAGE}:latest .
docker push ${USERNAME}/${IMAGE}:latest

#LC=$(git rev-parse --short HEAD)
#docker build -t seductive/ixapp:${LC} .
#docker push seductive/ixapp:${LC}


