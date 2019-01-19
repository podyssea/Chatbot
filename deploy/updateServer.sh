#!/usr/bin/env bash

set -e

rm -rf /home/ubuntu/dissertation

git clone git@gitlab.com/modelorona/dissertation.git

cd /home/ubuntu/dissertation
cd client
npm install
npm run build

sudo service nginx reload
