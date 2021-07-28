import os

import requests

GITHUB_TOKEN = os.environ['TOKEN_GITHUB']


def print_workflow_status():
    workflow = "blank.yml"
    endpoint = "https://api.github.com/repos/angelicalimazup/testPipes/actions/workflows/" + workflow + "/runs"
    headers = {"accept": "application/vnd.github.v3+json",
               "content-type": "application/json",
               "authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(endpoint, headers=headers).json()
    print(r['workflow_runs'])


if __name__ == '__main__':
    print_workflow_status()
