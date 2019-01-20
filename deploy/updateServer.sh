#!/usr/bin/env bash

set -e

rm -rf /home/ubuntu/dissertation

git clone git@gitlab.com:modelorona/dissertation.git

cd ~/dissertation/client
npm install
npm run build

cd ~
source projectenv/bin/activate
cd ~/dissertation/server
fuser -k -n tcp 5000
pip install -r requirements.txt
python app.py &

sudo service nginx reload
