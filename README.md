# Linear Client

A Python client for interacting with the [Linear](https://linear.app) GraphQL API.

## Features

- Authenticate with your Linear API token
- Run GraphQL queries and mutations
- Fetch viewer info, issues, and update issue status
- Move issues to "Completed" workflow state

## Installation

```bash
# Clone the repo
git clone https://github.com/tbille/linear-client.git
cd linear-client

# Install dependencies using Poetry
poetry install

## Usage

```python
from linear_client.client import LinearClient
from linear_client.operations import get_viewer

client = LinearClient(token="your_linear_api_token")
viewer_op = get_viewer()
response = client.execute(viewer_op)
print(response)
```

## Move Issue to Completed

```python
from linear_client.operations import (
    move_issue_to_completed,
    update_issue_workflow_state
)

# Step 1: Fetch states
op = move_issue_to_completed("issue-id")
data = client.execute(op)

# Step 2: Find 'Completed' state ID
states = data['issue']['team']['workflowStates']
completed = next((s for s in states if s['name'] == 'Completed'), None)

# Step 3: Update issue
if completed:
    update_op = update_issue_workflow_state("issue-id", completed['id'])
    result = client.execute(update_op)
    print(result)
```

## Running Tests

```python
poetry run pytest
```