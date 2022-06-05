#imports
import requests

class RiotAPI(object):
    def __init__(self, riotApiKey):
        self.riotApiKey = riotApiKey
    def _request(self, params={}):
        args = {'api_key': self.riotApiKey}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/JigglyJo/GAMRE",
            params=args
        )
        return response.json()
    

