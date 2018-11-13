#!/bin/sh
#set -ex

# docker hub username
USERNAME=organization-name
# image name
IMAGE=tennapp

# ensure we're up to date
git pull

# bump version
docker run --rm -v "$PWD":/app treeder/bump patch
version=`cat ./VERSION`
echo "version: $version"

# run build
# ./push.sh
docker build -t ${USERNAME}/${IMAGE}:latest .

# tag it
git add -A
git commit -m "version $version"
#git tag -a "$version" -m "version $version"
git push
#git push --tags
docker tag $USERNAME/$IMAGE:latest $USERNAME/$IMAGE:$version
# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$version