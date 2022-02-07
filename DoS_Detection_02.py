import subprocess
import re
p = subprocess.Popen(["ping","192.168.144.13","-c 1"], stdout=subprocess.PIPE)
#if p is None: return None 
res=p.communicate()[0]
if p.returncode > 0:
    print('server error')
else:
    pattern = re.compile('TTL=\d*')
    print(pattern.search(str(res)).group())