import os
import requests
import time

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']
HASH_COMMIT = 'f678c8e214535cb2eec325d90ef0cf57d64bc8e4' #os.environ['SOURCE_COMMIT']

def workflow_status(workflowFile):
    #endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/"+ workflowFile + "/runs"
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/commits/"+HASH_COMMIT+"/status"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()
    return r#['workflow_runs'][-1]['status']


if __name__ == '__main__':
    workflowFile = "testFailWorkflow.yml"
    # while workflow_status(workflowFile) == 'queued':
    #     print(workflow_status(workflowFile))
    #     time.sleep(2)

print(workflow_status(workflowFile))
