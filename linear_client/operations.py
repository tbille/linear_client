from sgqlc.operation import Operation
from .schema import schema

def get_viewer():
    op = Operation(schema.Query)
    op.viewer.id()
    op.viewer.name()
    return op

def get_issues(first=10):
    op = Operation(schema.Query)
    issues = op.issues(first=first)
    issues.nodes.id()
    issues.nodes.title()
    return op

def update_issue_workflow_state(issue_id: str, completed_state_id: str):
    """Creates a mutation operation to update the issue to the completed workflow state."""

    op = Operation(schema.Mutation)
    input_data = {
        'id': issue_id,
        'input': {
            'workflowStateId': completed_state_id
        }
    }

    issue_update = op.issue_update(**input_data)
    issue_update.success()
    issue_update.issue.id()
    issue_update.issue.title()
    issue_update.issue.workflow_state.id()
    issue_update.issue.workflow_state.name()

    return op