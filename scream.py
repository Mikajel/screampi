import sys
import json

from src.request.request import Alert
from src.sound.sound import sound_test

def sanitize_input(**kwargs) -> dict:

    allowed_kwargs = [
        '--apikey',
        '--mode'
    ]

    sanitized_kwargs = {}

    for key, value in kwargs.items():
        
        if key not in allowed_kwargs:
            print(f'Unknown input attribute: {key}')
            print('Aborting execution')
            exit(1)

        else:
            sanitized_kwargs[key.lstrip('-')] = value

    return sanitized_kwargs

def apply_defaults(**kwargs) -> dict:

    if 'mode' not in kwargs.keys():
        kwargs['mode'] = 'office'
        print(f'Mode not specified - defaulting to \'{kwargs["mode"]}\'')
    
    if 'apikey' not in kwargs.keys():
        
        try:
            with open('apikey') as api_key_file:
                kwargs['apikey'] = api_key_file.read()
        
        except IOError:
            print('API-key not provided on-start')
            print('API-key file not available[missing/permissions/corrupted]')
            print('Aborting execution')
            exit(1)

    return kwargs


def main(**kwargs):

    kwargs = sanitize_input(**kwargs)
    kwargs = apply_defaults(**kwargs)
    
    print('Runtime settings:')
    [print(f'\t{key}={value}') for key, value in kwargs.items()]
    print('')

    # alerts = Alert.get_alert_list(api_key=kwargs['apikey'])
    
    # [print(alert) for alert in alerts]

    # example_alert = Alert.get_alert_by_identifier(
    #     api_key=kwargs['apikey'],
    #     id_type='id',
    #     id_value='3fe25743-c233-456d-8d9d-5c28ae144735-1561360443878'
    #     )

    # print(example_alert)

    # example_count = Alert.get_alert_count(api_key=kwargs['apikey'])
    # print(example_count)

    sound_test()

if __name__ == '__main__':

    main(**dict(arg.split('=') for arg in sys.argv[1:]))
