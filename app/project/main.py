from time import sleep
import sys

n = 0
limit = int(sys.argv[1])

while True:
    n += 1
    print(n)
    sleep(0.5)
    if n >= limit:
        break
