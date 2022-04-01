import requests as r
import os
import orjson as json
from dotenv import load_dotenv

DEFAULT_API_URL = "https://api.nrfcloud.com/v1/"


class NrfAPI:
    def __init__(self, token=None, url: str = DEFAULT_API_URL):
        """Initialize the object

        Args:
            token (str, optional): [Nordic API token. If none are provided, the client will attempt to load it from the .env file if there is one. 
            If there are no .env file, an exception will be raised]. Defaults to None.
            url (str, optional): URL to the API. Defaults to https://api.nrfcloud.com/v1/".

        Raises:
            Exception: No Token provided
        """
        if not token:
            load_dotenv()
            token = os.getenv('NRF_API_TOKEN')
        if not token:
            raise Exception("No token provided")
        self.token = token
        self.url = url

    @staticmethod
    def simple_auth(token) -> dict:
        """Create header for Simple auth token.

        Args:
            token (str): API Token from Nordic Cloud

        Returns:
            dictionary: Authorization header for the request
        """
        return {'Authorization': f'Bearer {token}'}

    @staticmethod
    def jwt_auth(jwt):
        """Authorization for JWT

        Args:
            jwt (str): JQT token from Nordic Cloud

        Returns:
            dictionary: Authorization header for the request
        """
        return {'Authorization': f'Bearer {jwt}'}

    def get_devices(self):
        """Get list of devices .

        Returns:
            dict: JSON object from the API
        """
        token = self.simple_auth(self.token)
        url = f'{self.url}devices'
        return r.get(url, headers=token)

if __name__ == "__main__":
    api = NrfAPI(
                 )
    response = api.get_devices()
    data = json.loads(response.text)
