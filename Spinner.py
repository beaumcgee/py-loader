
import sys
import time
import threading
import itertools

class Spinner:
    def __init__(self, startText, stopText, delay=.1):
        self.startText = startText
        self.stopText = stopText
        self.spin = False
        self.delay = delay 
       
        self.thread = threading.Thread(target=self.displaySpinner, args=())
        

    def displaySpinner(self):
        spinner = itertools.cycle(['- ', '\\ ', '| ', '/ '])

        while self.spin:
            sys.stdout.write('\033[2K\033[1G')                      # clear the line
            sys.stdout.flush()                                      # display cleared line
            sys.stdout.write(self.startText + ' ' + next(spinner))  # write text and next spinner character to buffer
            sys.stdout.flush()                                      # display text 
            time.sleep(self.delay)                                  # delay before next spinner character
            

    def start(self):
        self.spin = True
        self.thread.start()

    def stop(self):
        self.spin = False
        self.thread.join()
        sys.stdout.write('\033[2K\033[1G') 
        sys.stdout.flush()
        sys.stdout.write(self.stopText + '\n')