from unittest import TestCase

from workflow_utils import workflow_status


class TestClass(TestCase):
    def test_fail_workflow(self):
        workflowFile = "failWorkflow.yml"
        assert "failure" == workflow_status(workflowFile)
