import requests

dummy_alert_link = 'https://api.eu.opsgenie.com/v2/alerts/'


class Alert(object):

    def __init__(self, alert_data):

        try:
            self._id = alert_data['id']
            self.tiny_id = alert_data['tinyId']
            self.alias = alert_data['alias']
            self.message = alert_data['message']
            self.status = alert_data['status']
            self.acknowledged = alert_data['acknowledged']
            self.seen = alert_data['seen']
            self.is_seen = alert_data['isSeen']
            self.tags = alert_data['tags']
            self.snoozed = alert_data['snoozed']
            if self.snoozed:
                self.snoozed_until = alert_data['snoozedUntil']
            self.count = alert_data['count']
            self.last_occured_at = alert_data['lastOccurredAt']
            self.created_at = alert_data['createdAt']
            self.updated_at = alert_data['updatedAt']
            self.source = alert_data['source']
            self.owner = alert_data['owner']
            self.priority = alert_data['priority']
            self.teams = alert_data['teams']
            self.repsonders = alert_data['responders']
            self.integration = alert_data['integration']
            self.report = alert_data['report']

        except KeyError:
            print('Failed to parse received Alert data')
            print(f'Object data dump: {alert_data}')

    def __str__(self):
        """Format the print of this object"""

        __str = ''
        __str += f'Alert [{self._id}]\n'

        for key, value in self.__dict__.items():

            if isinstance(value, list):
                __str += f'\t{str(key)}\n'
                for item in value:
                    __str += f'\t - {str(value)}\n'

            elif isinstance(value, dict):
                __str += f'\t{str(key)}\n'
                for inner_key, inner_value in value.items():
                    __str += f'\t - {str(inner_key).ljust(17, ".")}{str(inner_value)}\n'

            else:
                __str += f'\t{str(key).ljust(20, ".")}{str(value)}\n'
        
        __str += '\n'

        return __str

    @staticmethod
    def get_alert(api_key: str, id: int):
        pass

    @staticmethod
    def list_alerts(api_key: str) -> []:
        """Get list of alerts from API, construct object from them and return them"""

        headers = {'Authorization': 'GenieKey ' + api_key}
        r = requests.get(dummy_alert_link, headers=headers)

        return [Alert(alert_data=alert_data) for alert_data in r.json()['data']]
