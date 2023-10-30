#!/usr/bin/env python
import os
 
# os.environ["ATLAS_BROKER_HOST"] = "ws://localhost"
 
# os.environ["ATLAS_BROKER_PORT"] = "8092"
 
try:
 
    import heimdall
 
    heimdall.start(apikey="b0265c61-8ff5-4418-a354-a154197e4d1f") # if this is your new api key
 
except ImportError as e:
 
     print("Error importing Heimdall: ", e)

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'plane.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
