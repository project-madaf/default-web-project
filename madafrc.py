'''
This file is responsible for handling the general configuration of MADAF.
'''

from madaf.api.config.override import RCConfig

def main():

    '''
        main function is required.
    '''

    config = RCConfig()

    # Project directory layout.
    config.modify['Project-Layout'] = {
        'Root-Path':'.',
        'Apps-Path':'apps',
        'Configs-Path':'configs',
        'Tests-Path':'tests'
    }

    # Installed apps. This is to ensure that only these
    # apps can access MADAF and MADAF plugins.
    config.modify['Installed-Apps'] = [
        'hello_world',
        'madaf_http'
    ]
