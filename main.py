import os
import requests
import time

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']


def workflow_status(workflowFile):
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/" + workflowFile + "/runs"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()
    return r['workflow_runs'][-1]['status']


if __name__ == '__main__':
    workflowFile = "failWorkflow.yml"
    while workflow_status(workflowFile) == 'queued':
        print(workflow_status(workflowFile))
        time.sleep(2)

print(workflow_status(workflowFile))
