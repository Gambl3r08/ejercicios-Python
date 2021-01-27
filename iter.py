import time
import itertools

bucle = itertools.cycle("|/-")

for i in range(20):
    print("Downloading... {}".format(next(bucle)), end="\r")
    time.sleep(0.1)
    
print("\nDone.")