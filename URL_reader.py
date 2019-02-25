# PJ Mallery
# Assignment 6
# Python 3

import urllib.request, sys, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
try:
    handle = urllib.request.urlopen(url, context=ctx)
except:
    print('Not a valid URL.')
    sys.exit(0)

chunk_size = 512
limit = 3000  # variable to use to limit number of characters to print
size = 0  # variable to track total size of data transmitted
print_size = 0  # variable to track number of characters printed

while True:
    data = handle.read(chunk_size)
    size = size + len(data)
    if len(data) < 1: break
    if limit >= chunk_size:
        print(data.decode())
        limit = limit - chunk_size
        print_size = print_size + len(data)
    elif 0 < limit < chunk_size:
        data = data[:limit]  # limit last print out, only want number of characters in limit variable
        print(data.decode())
        print_size = print_size + len(data)
        limit = 0
    else:
        continue

print('Number of characters printed:', print_size)
print('Total number of characters:', size)
handle.close()
