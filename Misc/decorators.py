from functools import lru_cache
import time
from Leetcode.utils.utility import timer

import atexit

def destroy_objects():
    all_objs_destroyed = False
    while(not all_objs_destroyed):
        try:
            time.sleep(3)
            all_objs_destroyed=True
        except KeyboardInterrupt as ke:
            pass
    print('Destoryed objects')


#Runs in the end of the program execution
@atexit.register
def goodbye():
    destroy_objects()


@timer
@lru_cache(maxsize=None)
def fibonacci(n):
    res = [0, 1]
    for index in range(2, n):
        temp = res[-1] + 0
        time.sleep(2)
        res[-1] = res[-2] + res[-1]
        res[-2] = temp


from dataclasses import dataclass


class Payload:
    """Pl classes to implement this bad boy"""


@dataclass
class ApisvcPaylod(Payload):
    version: int
    min: int
    max: int


pl = ApisvcPaylod(version=1, min=2, max=22)

print(pl)
fibonacci(23)