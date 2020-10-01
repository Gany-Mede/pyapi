 #!/usr/bin/python3

import threading
import os
def first():
    for i in range(1000):
        print(f"From FIRST loop: {i}")

def two():
    for b in range(1000):
        print(f"From SECOND loop: {b}")

t1 = threading.Thread(target = first, name ='t1')
t2 = threading.Thread(target = two, name = 't2')

t1.start()
t2.start()

t1.join()
t2.join()

