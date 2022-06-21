'''

This file is used to configure MADAF settings.

'''

from madaf.api.config.override import AppConfig, AssignID

def general():

    '''
        This function configures the general behaviour of MEDAF.
    '''

    # Assign an ID to your app.
    AssignID('hello_world')
