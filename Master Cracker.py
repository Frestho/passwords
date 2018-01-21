#A combination of all crackers, optimalized to be the best at cracker passwords.
import time
pw = input("Enter your password: ")
start = time.time()
commonPws = open(commonpassword.txt).split()
words = open(words.txt).split()
totalAttempts = 0
def common():
    for i in range(0, len(commonPws)):
        
def bruteForce(mode, guesses):
    cracked = False #state of password cracking
    chars = mode #all the characters the the program will try
    charOn = [-1] #holds all the character values
    attempts = 0
    while not cracked:
        attempts += 1
        totalAttempts += 1
        if attempts > guesses:
            print("Brute force failed, going on to next cracking method.")
        #changes the right-most character of the password that is being attempted
        charOn[len(charOn) - 1] += 1
        
        #if any character in charOn is over the limit (in this case, ?), it switches it back to the beginning (a) and changes the previous character by 1
        for i in reversed(range(1, len(charOn))):
            if charOn[i] > len(chars)-1:
                charOn[i] = 0
                charOn[i-1] += 1
            
        #if the first character is z, then change it back to a and add a new character
        if charOn[0] > len(chars)-1:
            charOn[0] = 0
            charOn.append(0)
            
        #the current password attempt
        attempt = ""
        
        #decodes charOn into a string and store it in attempt
        for i in range(0, len(charOn)):
            attempt += chars[charOn[i]]
        
        #check if we got the password
        if attempt == pw:
            print("Your password was found! It is " + str(attempt) + ", right? It took me " + str(attempts) + " attempts to find it. It took " + str(round(time.time()-start, 2)) + " seconds.")
            cracked = True
def dict():
    
        
