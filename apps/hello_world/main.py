'''

This file is the main entry point into your program.

'''

from madaf.api.init import init
from madaf_http import gateway

def home():

    '''
        Linked to rootpage.
        Refer to ./configs/hello_world/route.py for
        more details.
    '''

    return "Hello, world!"

init(mount=gateway)
