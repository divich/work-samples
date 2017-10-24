###game that records your time to type a to z###


import time
start = "true"

#Instructions#
print ("\nINSTRUCTIONS\n1. When the countdown gets to zero type the alphabet!\n2. That is the only rule!")
input("Press Enter when ready.")
#looping
while start == "true":
    
    name = input("What is your name?: \n")
    name = name.split(' ')

    #Countdown#
    print ("Game Will Start in: ")
    print ("3")
    time.sleep(1)
    print ("2")
    time.sleep(1)
    print ("1")
    time.sleep(1)

    #Start Time#
    startTime = time.time()

    #Alphabet Input#
    alphabet = input("Go! Go! Go! Type in the Alphabet: \n")
    alphabet = alphabet.lower()
    
    #Validation#
    if alphabet == "abcdefghijklmnopqrstuvwxyz":
        #End Time#
        endTime = time.time()

        #Score#
        score = endTime - startTime
        score = round(score, 1)

        #Output Score#
        print ("CONGRATULATIONS " +  name[0] + "\nYour time was - " + str(score) + "seconds")
        
    else:
        print ("You made a mistake!")

    #Restart#
    restart = input("say yes  to restart: \n")
    if restart == "YES" or "yes":
        start = "true"
    else:
        start = "false"

























    
