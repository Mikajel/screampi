import requests

dummy_alert_link = 'https://api.eu.opsgenie.com/v2/alerts'


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
    def get_alert_by_identifier(api_key: str, id_type: str, id_value: str) -> object:
        """
        Get alert from API by its id, construct object from it and return Alert
        """

        headers = {'Authorization': 'GenieKey ' + api_key}
        response = requests.get(
            url=dummy_alert_link + f'/{id_value}?identifierType={id_type}', 
            headers=headers
            )

        print(response.json())
        return Alert(response.json()['data'])

    @staticmethod
    def get_alert_list(api_key: str) -> []:
        """
        Get list of alerts from API, construct object from them and return them
        TODO: querying for server-side filtering
        """

        headers = {'Authorization': 'GenieKey ' + api_key}
        response = requests.get(dummy_alert_link, headers=headers)

        return [Alert(alert_data=alert_data) for alert_data in response.json()['data']]

    @staticmethod
    def get_alert_count(api_key: str) -> int:
        """
        Get amount of existing alerts
        TODO: querying for server-side filtering[searchIdentifier/searchIdentifierType] (https://docs.opsgenie.com/docs/alert-api#section-count-alerts)
        """

        headers = {'Authorization': 'GenieKey ' + api_key}
        response = requests.get(dummy_alert_link + '/count', headers=headers)

        print(response.json())
        return response.json()['data']['count']
