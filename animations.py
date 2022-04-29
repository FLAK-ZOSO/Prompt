#!usr/bin/env Python3
import time


def loadingTimed(ms: int) -> None:
    wait: float = ms/10000
    for i in range(100):
        time.sleep(wait) # So it takes <ms>ms for n sleeps
        print(f"[ {'|'*i}{' '*(100-i)} ] {i}%", end='\r')
    print(f"[ {'|'*100} ] 100%")


loadingTimed(5000)