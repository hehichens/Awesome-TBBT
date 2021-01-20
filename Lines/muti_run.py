"""
run get_contents.py for many times
edit by hichens
"""

import os
import time

if __name__ == "__main__":
    # defualt is 100. it's totally enough
    for i in range(100):
        os.system("python get_contents.py")
        time.sleep(1)