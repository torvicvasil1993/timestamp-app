# timestamp-app

oc create -f ./timestamp-app-template.yaml 

oc get templates

oc new-app --template timestamp-app-template --source-secret=pocs-rpa -p BRANCH_NAME=master -p APP_GIT_URL=https://gitlab.com/grupo-globo/tecnologia/hdg/jcorp/iap/automacao/pocs-rpa -p PROJECT_NAME=torvicvasil-dev -p APP_NAME=timestamp-app
