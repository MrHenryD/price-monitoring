#!/bin/bash

BASE=henry/voracity
VERSION=$1

if [ $# -eq 0 ]; then
    echo "No version tag provided"
    exit 1
fi

echo "Building image $BASE:$VERSION..."
docker build -t $BASE:$VERSION .
echo "Finished building image"
