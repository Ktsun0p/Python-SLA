import requests
from methods.getVersion import get_version
from methods.getChampByKey import get_champ_by_key
import json

champion_by_id_cache = {}
champion_json = {}

masteries_emojis = [
    "<:m1:1160313061106782208>",
    "<:m2:1160313059001237595>",
    "<:m3:1160313056102985881>",
    "<:m4:1160313054098104421>",
    "<:m5:1160313051489259683>",
    "<:m6:1160313049937358868>",
    "<:m7:1160313046883897364>"
]

def get_masteries(summoner_id, region, key, language="en_US"):
    last_ver = get_version()
    masteries = requests.get(f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{summoner_id}?api_key={key}').json()
   
    champ_emojis = requests.get('https://ktsun0p.github.io/cakebot-simple-api/champs.json').json()
    top_masteries = []

    if masteries:
        counter = 0
        for mastery in masteries:
            if counter >= 10:
                break
            fm = get_champ_by_key(champion_by_id_cache, champion_json, mastery['championId'], language)
            fm1 = mastery['championLevel']
            pfm1 = mastery['championPoints']
            champ_emj = "<:Toto_Bug:1019280617105522729>" if str(mastery['championId']) not in champ_emojis else champ_emojis[str(mastery['championId'])]['icon']

            top_masteries.append({
                'name': fm['name'],
                'id': fm['id'],
                'slogan': fm['title'],
                'level': fm1,
                'levelEmoji': masteries_emojis[fm1 - 1],
                'emoji': champ_emj,
                'points': pfm1,
                'full': f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{fm["id"]}_0.jpg',
                'square': f'http://ddragon.leagueoflegends.com/cdn/{last_ver}/img/champion/{fm["id"]}.png'
            })
            counter +=1
    return top_masteries