from unittest import TestCase
from workflow_utils import workflow_status


class TestClass(TestCase):
    def test_fail_workflow(self):
        workflow_file = "failWorkflow.yml"
        assert "failure" == workflow_status(workflow_file)

    def test_success_workflow(self):
        workflow_file = "successWorkflow.yml"
        assert "success" == workflow_status(workflow_file)