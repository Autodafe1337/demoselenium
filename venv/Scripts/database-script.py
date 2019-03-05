#!C:\Users\l2meg\PycharmProjects\demoselenium\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rspec==0.0.3','console_scripts','database'
__requires__ = 'rspec==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rspec==0.0.3', 'console_scripts', 'database')()
    )
