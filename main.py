import timer
from playsound import playsound

def twentyRule(key):
    
    while key == 1:
        timer.countDown(1200)
        playsound('lookaway.mp3')
        timer.countDown(20)
        playsound('resume.mp3')

while (True):

    key = int(input("Enter 1 to start and 0 to end:"))
    if key == 1:
        twentyRule(key)

