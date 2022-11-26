#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ROX.so ROYAL.so')
except:
    pass
os.system('rm -rf ROX.so ROYAL.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ROX.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exxx/blob/main/ROX.cpython-311.so?raw=true -o ROX.so') 
        __import__("ROX").chigozie()
    else:
        __import__("ROX").chigozie()

elif bit == '32bit':
    if not os.path.isfile('ROYAL.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exxx/blob/main/ROYAL.cpython-311.so?raw=true -o ROYAL.so') 
        __import__("ROYAL").chigozie()
    else:
        __import__("ROYAL").chigozie()
