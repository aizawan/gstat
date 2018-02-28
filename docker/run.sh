#!/bin/bash

cd /src
python3 manage.py runserver 0.0.0.0:8888

while true
do
  sleep 1
done

