
# get username and computername from environment
import os
username = os.environ.get('USERNAME', 'Unknown')
world = os.environ.get('COMPUTERNAME', 'World')

# get python version 
import sys
python_version = sys.version

# print greeting
print("Hello %s from %s!" % (username, world))
print("Python version: %s" % python_version)

## keep container running
# import time
# while True:
#     time.sleep(60)
