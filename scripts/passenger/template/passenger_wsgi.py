projectname = 'bashoneliners'
virtualenv_root = '/home/janoscom/virtualenv/' + projectname

import sys
import os

INTERP = os.path.join(virtualenv_root, 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.path.join(os.getcwd(), projectname))
os.environ['DJANGO_SETTINGS_MODULE'] = projectname + '.prod_settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
