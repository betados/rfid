import threading
import time


class Reader(object):
    def __init__(self):
        self.__code = None
        self.__t = None
        self.done = False

        t = threading.Thread(target=self.read)
        t.start()

    @property
    def code(self):
        return self.__code

    def read(self):
        while not self.done:
            self.__code = raw_input('Pase su tarjeta')
            print 'Your code is:', self.__code
            if self.__code == 'exit':
                break


reader = Reader()

while True:
    time.sleep(0.5)
    print 'Hago otras mierdas'
    if reader.code == 'exit':
        break
