import os
import requests
import time

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']
HASH_COMMIT = os.environ['SOURCE_COMMIT']

def workflow_status(workflowFile):
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/"+ workflowFile + "/runs"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()

    for run in r['workflow_runs']:
        if run['head_sha'] == HASH_COMMIT:
            workflow = run
    print(workflow)
    return workflow['conclusion']


if __name__ == '__main__':
    time.sleep(60)
    workflowFile = "failWorkflow.yml"
print(workflow_status(workflowFile))
