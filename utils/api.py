import keyring
import requests


class Api():

    def __init__(self, base_url, query, header_key, user):

        self.base_url = base_url
        self.query = query
        self.user = user

        self.api_key = keyring.get_password(user, "api_key")
        self.header = {header_key: self.api_key}
    def get_response(self, endpoint):

        return requests.request("GET",
                                self.base_url + endpoint,
                                headers=self.header,
                                params=self.query).json()


        

