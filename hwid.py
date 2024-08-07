import os
import hashlib
import platform
print(hashlib.sha256((os.getenv("COMPUTERNAME")+os.getenv("USERNAME")+str(platform.architecture())).encode()).hexdigest())
os.system("pause")