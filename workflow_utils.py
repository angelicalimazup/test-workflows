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

    workflow_complete = False
    while not workflow_complete:
        time.sleep(5)
        r = requests.get(endpoint, headers=headers).json()
        for run in r['workflow_runs']:
            if run['head_sha'] == HASH_COMMIT:
                workflow = run
                break
        if workflow['workflow_runs'].get('conclusion') != 'None':
            workflow_complete = True

    print(workflow)
    return workflow['conclusion']
