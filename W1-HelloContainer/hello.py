# get running os
import platform
this_os = platform.system()

# get username and computername from environment
import os
if this_os == "Windows":
    username = os.environ.get("USERNAME", "unknown")
    computername = os.environ.get("COMPUTERNAME", "World")
else:
    username = os.environ.get("USER", "unknown")
    computername = os.environ.get("HOSTNAME", "World")
    
# get python version 
import sys
python_version = sys.version

# print greeting
print("Hello %s from %s!" % (username, computername))
print("OS: %s" % this_os)
print("Python version: %s" % python_version)

## keep container running
import time
while True:
    time.sleep(60)