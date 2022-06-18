'''
    Configure routing.
'''

from madaf_http.api.routing import link, config
from apps.hello_world.main import home

def route():

    '''
        This function configures the routing.
    '''

    # This will configure the root page.
    root_page = link('/', home)
    # Default: text/plain
    root_page.config['Content-Type']['media-type'] = 'text/plain'
    # Default: UTF-16
    root_page.config['content_type']['charset'] = 'UTF-8'

    # This will configure the gateway option.
    config['gateway'] = 'builtin'
