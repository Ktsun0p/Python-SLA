import json
from methods.getSummonerByName import get_summoner_by_name

class riot_api:
    def __init__(self, api_key):
        self.key = api_key

    class Summoner:
        def __init__(self, api_instance, name, tag, region):
            self.api_instance = api_instance
            self.name = name
            self.tag = tag
            self.region = region

        def getLolProfile(self):
            return get_summoner_by_name(name=self.name, tag=self.tag, region= self.region,apiInstance=self.api_instance)

    def create_summoner(self, name, tag, region):
        return self.Summoner(self, name, tag, region)
