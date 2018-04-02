import os
import time

def get_all(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for x in files:
            fname = root + x
            filectime = os.stat(fname).st_ctime
            if (filectime-nowtime > 3600*5):
                os.remove(fname)

nowtime = time.time()
get_all('./cache/')
