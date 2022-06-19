'''
    Configure routing.
'''

from madaf.api.config.override import AppConfig

from apps.hello_world.main import home

def route():

    '''
        This function configures the routing.
    '''

    config = AppConfig('madaf_http')

    # This will configure the root page.
    config.modify['link'] = {
        '/': home
    }

    # Default:
    # config.modify['/]['Content-Type] = {
    #   'media-type': 'text/plain',
    #   'charset': 'utf-8'
    # }
    config.modify['/']['Content-Type']['media-type'] = 'text/plain'
    config.modify['/']['Content-Type']['charset'] = 'UTF-8'

    # This will configure the gateway option.
    config.modify['gateway'] = 'builtin'
