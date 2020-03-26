#import sys

#for line in sys.stdin:
#   print(line)

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
with open("html.txt", "w", encoding="utf-8") as f:
    f.write(str(html))