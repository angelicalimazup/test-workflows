import json
import os
import time
import requests

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']
HASH_COMMIT = os.environ['SOURCE_COMMIT']


def workflow_status(workflow_file):
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/" + workflow_file + "/runs"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()

    while r['workflow_runs'].get('conclusion', None) is None:
        r = requests.get(endpoint, headers=headers).json()
        time.sleep(5)

    for run in r['workflow_runs']:
        if run['head_sha'] == HASH_COMMIT:
            workflow = run
            break

    print(workflow)
    return workflow['conclusion']


