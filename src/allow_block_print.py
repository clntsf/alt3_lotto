import sys
import os
from typing import Callable

def allow_block_print(func: Callable):
    """
    Decorator function that allows functions to be run with
    an optional parameter to block internal prints.

    Not actually useful for this project per se, but I played
    around with it to see if I could do it before deciding it
    wasn't needed here
    """
    def with_block_print(*args, block: bool = False, **kwargs):
        if block:
            tmp = sys.__stdout__
            sys.stdout = open(os.devnull,"w")

        func_vals = func(*args,**kwargs)

        if block: sys.stdout = tmp

        return func_vals

    return with_block_print
