import os
import sys
import config.settings

# create settings object corresponding to specified env
APP_ENV = os.environ.get('APP_ENV', 'Dev')

_current = getattr(sys.modules['config.settings'], '{0}Config'.format(APP_ENV))()

# copy attributes to the module for convenience
for f in dir(_current):
    if not '__' in f:
        val = getattr(_current, f)
        setattr(sys.modules[__name__], f, val)