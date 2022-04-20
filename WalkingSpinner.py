
import sys
import time
import threading
import itertools

class WalkingSpinner:
    def __init__(self, startText, stopText, repeats=5, delay=.1):
        self.startText = startText
        self.stopText = stopText
        self.repeats = repeats
        self.delay = delay 
        self.spin = False
       
        self.thread = threading.Thread(target=self.displaySpinner, args=())

    def buildBlankSpaces(self, count):
        blankSpaces = ''

        if count == 0:
            return blankSpaces
        else:
            for index in range(count):
                blankSpaces += ' '
            
            return blankSpaces


    def displaySpinner(self):
        spinnerChars = [' -', ' \\', ' |', ' /']
        spinner = itertools.cycle(spinnerChars)
        count = 0

        while self.spin:
            sys.stdout.write('\033[2K\033[1G')                      # clear the line
            sys.stdout.flush()                                      # display cleared line
            sys.stdout.write(self.startText + self.buildBlankSpaces(count) + next(spinner) + ' ')  # write text and next spinner character to buffer
            sys.stdout.flush()                                      # display text 
            time.sleep(self.delay)                                  # delay before next spinner character

            if count < len(spinnerChars) * self.repeats:
                count += 1
            else:
                count = 0
            

    def start(self):
        self.spin = True
        self.thread.start()

    def stop(self):
        self.spin = False
        self.thread.join()
        sys.stdout.write('\033[2K\033[1G') 
        sys.stdout.flush()
        sys.stdout.write(self.stopText + '\n')