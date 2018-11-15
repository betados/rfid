import threading
import time


def read():
    code = raw_input('Pase su tarjeta')
    print 'Your code is:', code


def run_read():
    t = threading.Thread(target=read)
    t.start()
    return t


t = run_read()

while True:
    if not t.isAlive():
        t = run_read()
    time.sleep(0.5)
    print 'Hago otras mierdas'
