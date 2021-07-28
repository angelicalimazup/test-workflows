from unittest import TestCase

from workflow_utils import workflow_status


class TestClass(TestCase):
    def test_fail_workflow(self):
        workflowFile = "failWorkflow.yml"
        workflow = workflow_status(workflowFile)
        print(workflow)
        assert "failure" == workflow_status(workflow)
