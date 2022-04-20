
import sys
import time
import threading

class Dots:
    def __init__(self, startText, stopText, numDots=20, delay=.1):
        self.startText = startText
        self.stopText = stopText
        self.numDots = numDots
        self.delay = delay
        self.loading = False
       
        self.thread = threading.Thread(target=self.displaySpinner, args=())
    
    def gen_dots(self, count):
        dots = ''

        if count == 0:
            return ''
        else: 
            for index in range(count):
                dots += '.'
            
            return dots

    def displaySpinner(self):
        count = 0

        while self.loading:
            sys.stdout.write('\033[2K\033[1G')                                      # clear the line
            sys.stdout.flush()                                                      # display cleared line
            sys.stdout.write(self.startText + ' ' + self.gen_dots(count) + ' ')     # write text and next spinner character to buffer
            sys.stdout.flush()                                                      # display text 
            time.sleep(self.delay)                                                  # delay 

            if count < self.numDots:
                count += 1
            else:
                count = 0
            

    def start(self):
        self.loading = True
        self.thread.start()

    def stop(self):
        self.loading = False
        self.thread.join()
        sys.stdout.write('\033[2K\033[1G') 
        sys.stdout.flush()
        sys.stdout.write(self.stopText + '\n')