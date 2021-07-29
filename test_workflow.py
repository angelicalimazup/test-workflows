from unittest import TestCase
from workflow_utils import workflow_status


class TestClass(TestCase):
    def test_fail_workflow(self):
        workflow_file = "failWorkflow.yml"
        assert "failuaare" == workflow_status(workflow_file)
