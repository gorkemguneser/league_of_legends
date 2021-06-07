import requests
import riot_consts as consts
import riot_api_key as riot_api_key

class riot_api(object):
    
    def __init__(self, api_key=riot_api_key.KEY, region=consts.REGIONS['TR']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items:
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url),
            params=args
            )
        print(response.url)
        return response.json()
    
    def get_summoner_by_name(self, name):
        api_url = consts.URL['summoner_by_name'].format(
            version=consts.API_VERSIONS['summoner'],
            names=name
        )
        self._request(api_url)