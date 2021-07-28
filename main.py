import os
import requests
import time

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']
HASH_COMMIT = os.environ['SOURCE_COMMIT']

def workflow_status(workflowFile):
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/"+ workflowFile + "/runs"
    #endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/statuses/"+HASH_COMMIT
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()

    for v in r['workflow_runs']:

        if v['head_sha'] == HASH_COMMIT:
            workflow = v

    return workflow


if __name__ == '__main__':
    time.sleep(60)
    workflowFile = "failWorkflow.yml"
    # while workflow_status(workflowFile) == 'queued':
    #     print(workflow_status(workflowFile))
    #     time.sleep(2)
print(workflow_status(workflowFile))
