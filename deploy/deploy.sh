#!/usr/bin/env bash
set -e
eval $(ssh-agent -s)
echo "$PRIVATE_KEY" | tr -d '\r' | ssh-add - > /dev/null

./deploy/disableHostKeyChecking.sh

DEPLOY_SERVERS=$DEPLOY_SERVERS

ALL_SERVERS=(${DEPLOY_SERVERS//,/ })
echo "ALL_SERVERS ${ALL_SERVERS}"

# echo in lines to create flaskenv file on the server
sed -i '2icat .flaskenv' ./deploy/updateServer.sh
sed -i '2iecho SECRET_KEY="$SECRET_KEY" >> .flaskenv' ./deploy/updateServer.sh
sed -i '2iecho FLASK_APP="$FLASK_APP" >> .flaskenv' ./deploy/updateServer.sh
sed -i '2iecho FLASK_ENV="$FLASK_ENV" >> .flaskenv' ./deploy/updateServer.sh
sed -i '2iecho DATABASE_URL="$DATABASE_URL" >> .flaskenv' ./deploy/updateServer.sh
sed -i '2i touch .flaskenv' ./deploy/updateServer.sh

for server in "${ALL_SERVERS[@]}"
do
  echo "deploying to ${server}"
  ssh ubuntu@${server} 'bash' < ./deploy/updateServer.sh
done

