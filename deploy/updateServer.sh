#!/usr/bin/env bash

set -e

#rm -rf /home/ubuntu/dissertation

#git clone git@gitlab.com:modelorona/dissertation.git
cd /home/ubuntu/dissertation
git add .
git stash
git pull

cd /home/ubuntu/dissertation/client
npm install
npm run build

cd ~
source projectenv/bin/activate
cd ~/dissertation/server
fuser -k -n tcp 5000
pip install -r requirements.txt
python app.py &> output.log &

#sudo service nginx reload
