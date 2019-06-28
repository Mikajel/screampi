import sys
import json

from src.request.request import Alert

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

    alerts = Alert.list_alerts(api_key=kwargs['apikey'])
    
    [print(alert) for alert in alerts]

    

if __name__ == '__main__':

    main(**dict(arg.split('=') for arg in sys.argv[1:]))
