import os
import requests
from sgqlc.endpoint.requests import RequestsEndpoint


class LinearClient:
    def __init__(self, token: str = None):
        self.token = token or os.getenv('LINEAR_API_TOKEN')
        if not self.token:
            raise ValueError("API token must be provided.")

        # Create a custom requests.Session if needed
        session = requests.Session()
        session.headers.update({
            'Authorization': f'{self.token}',
            'Content-Type': 'application/json'
        })

        self.endpoint = RequestsEndpoint('https://api.linear.app/graphql', session=session)

    def execute(self, operation):
        return self.endpoint(operation)