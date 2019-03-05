#!C:\Users\l2meg\PycharmProjects\demoselenium\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'behave-py3==1.2.5.post2014122202','console_scripts','behave'
__requires__ = 'behave-py3==1.2.5.post2014122202'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('behave-py3==1.2.5.post2014122202', 'console_scripts', 'behave')()
    )
