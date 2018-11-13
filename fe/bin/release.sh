#!/bin/sh
#set -ex

# docker hub username
USERNAME=seductive
# image name
IMAGE=eth-signals

# ensure we're up to date
git pull

# Build front end and moved static to web container
DOCKER_CMD="docker-compose run -e API_BASE_URL=${API_BASE_URL} -e HEAD_TITLE='${HEAD_TITLE}' -e HEAD_DESCRIPTION='${HEAD_DESCRIPTION}'  fe bash -c 'npm run build --report'"
#echo ${DOCKER_CMD}

rm -rf dist && cd .. && eval ${DOCKER_CMD}

cd fe

# bump version
docker run --rm -v "$PWD":/app treeder/bump patch
version=`cat VERSION`
echo "nuxt-web version: $version"

# run build
docker build -t ${USERNAME}/${IMAGE}:latest .

# tag it
git add -A
git commit -m "nuxt-web version $version"
#git tag -a "$version" -m "version $version"
git push
#git push --tags
docker tag $USERNAME/$IMAGE:latest $USERNAME/$IMAGE:$version
# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$version

