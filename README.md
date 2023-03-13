# timestamp-app

~/timestamp-app$ oc create -f ./timestamp-app-template.yaml 
template.template.openshift.io/timestamp-app-template created

~/timestamp-app$ oc get templates

~/timestamp-app$ oc describe template timestamp-app-template


oc new-app --template timestamp-app-template -p BRANCH_NAME=main -p APP_GIT_URL=https://github.com/torvicvasil1993/timestamp-app -p PROJECT_NAME=torvicvasil-dev -p APP_NAME=timestamp-app
