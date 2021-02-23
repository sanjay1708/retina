import time 
from threading import *
from playsound import playsound


class timer(Thread):

    def countDown(self,t): 
	 
	    while t: 
		    mins, secs = divmod(t, 60) 
		    timer = '{:02d}:{:02d}'.format(mins, secs) 
		    print(timer, end="\r") 
		    time.sleep(1) 
		    t -= 1

    def run(self):
        self.countDown(12)
        playsound('audio/lookaway.mp3')
        self.countDown(20)
        playsound('audio/resume.mp3')


 