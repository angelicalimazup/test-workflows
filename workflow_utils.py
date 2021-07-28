import os
import requests

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']
HASH_COMMIT = os.environ['SOURCE_COMMIT']


def workflow_status(workflowFile):
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/" + workflowFile + "/runs"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()

    for run in r['workflow_runs']:
        if run['head_sha'] == HASH_COMMIT:
            workflow = run

    #time.sleep(60)
    return workflow['conclusion']

