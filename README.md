# text_classification_api
SAP WEB API for classification of bank transaction type.
___
### Deploying the app:
1. Download Cloud Foundry CLI: https://docs.cloudfoundry.org/cf-cli/install-go-cli.html
2. Go to the project root from CLI
3. From the CLI run `cf login`:
- API endpoint: https://api.cf.eu10.hana.ondemand.com
- CF email: name.soname@sap.com
- CF password: 
4. To deploy an app run `cf push`

___
### Testing the app:
Option 1 (using Postman):
1. Open Postman
2. Import file testing_postman.json
3. Send the request

Option 2 (manually):
Send POST request with the following options:
1. url: https://mlnlmk.cfapps.eu10.hana.ondemand.com/api/classify
2. Headers:
  - Key: Content-Type
  - Value: application/json
3. Body: {"text": "text to classify"}
