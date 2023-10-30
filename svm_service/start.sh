#!/bin/bash
app="svm_service"
docker build -t ${app} .
docker run -d -p 56731:80 \
    --name=${app} \
    -v $PWD:/app ${app}
