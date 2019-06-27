import requests
import json

dummy_link = 'https://api.eu.opsgenie.com/v2/alerts/'

def proto_get_alerts(api_key: str):
    
    headers = {'Authorization': 'GenieKey ' + api_key}
    r = requests.get(dummy_link, headers=headers)

    print(json.dumps(r.json(), indent=4))

class Alert(object):

    def __init__(
        self, 
        id: str,
        tiny_id: str, 
        message: str,
        status: str,
        acknowledged: bool,
        is_seen: bool,
        tags: [str],
        snoozed: bool,
        snoozed_until: str,

        ):
        
        print('Dummy alert init')

    @classmethod
    def list_alerts() -> []:

        return []
