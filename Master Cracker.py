#A combination of all crackers, optimalized to be the best at cracker passwords.
import time
pw = input("Enter your password: ")
start = time.time()
commonPws = open("commonpasswords.txt").readlines()
for i in range(0, len(commonPws)):
    commonPws[i] = commonPws[i].rstrip()
words = open("words.txt").readlines()
for i in range(0, len(words)):
    words[i] = words[i].rstrip()
wordOn = [-1]
totalAttempts = 0
def common():
    for i in range(0, len(commonPws)):
        if commonPws[i] == pw:
            print("Your password \"" + commonPws[i] + "\" has been found. It was number " + str(i + 1) + " on the most common password list.")
            return
    print("Password not found on the common password list, onto next method...")
def bruteForce(mode, guesses):
    global totalAttempts
    cracked = False #state of password cracking
    chars = mode #all the characters the the program will try
    charOn = [-1] #holds all the character values
    attempts = 0
    while not cracked:
        attempts += 1
        if attempts > guesses:
            print("Brute force failed, going on to next cracking method.")
            return
        totalAttempts += 1
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
            return
def dictionary(caps, guesses):
    attempts = 0
    unsolved = True
    while unsolved:
        attempts += 1
        if attempts > guesses:
            print("Dictionary attack failed, going on to next cracking method.")
        totalAttempts += 1
        wordOn[len(wordOn) - 1] += 1
        for i in reversed(range(1, len(wordOn))):
            if wordOn[i] > len(words) - 1:
                wordOn[i] = 0
                wordOn[i - 1] += 1
        
        #adds another item to the end of the word list if the first word is "overflowed"
        if wordOn[0] > len(words) - 1:
            wordOn[0] = 0
            wordOn.append(0)
        
        attempt = ""
        for i in range (0, len(wordOn)):
            attempt += words[wordOn[i]]

        if attempt == pw:
            print("Your password \"" + attempt + "\" has been found! It took " + str(attempts) + " attempts and " + str(round(time.time() - start, 2)) + " seconds.")
            unsolved = False
def combo(numbers, guesses):
    wordOn = [-1]
    #adds numbers if the bare dictionary attack isn't working
    numbers = []
    attempts = 0
    unsolved = True
    while unsolved: 
        attempts += 1
        if attempts > guesses:
            print("Combination attack failed, going on to next cracking method.")
        totalAttempt += 1
        wordOn[len(wordOn) - 1] += 1
        """
        for i in reversed(range(1, len(wordOn)):
            if wordOn[i] > len(words):
                wordOn[i] = 0
                wordOn[i - 1] += 1
        """
        #adds another item to the end of the word list if the first word is "overflowed"
        if wordOn[0] > len(words) - 1:
            wordOn[0] = 0
            numbers.append(0)
        if len(numbers) > 0:
            numbers[len(numbers) - 1] += 1
        attempt = ""
        for i in range (0, len(wordOn)):
            attempt += words[wordOn[i]]
        if len(numbers) > 0:
            attempt += str(numbers[0])
        if attempt == pw:
            print("Your password \"" + attempt + "\" has been found! It took " + str(attempts) + " attempts and " + str(round(time.time() - start, 2)) + " seconds to find your password.")
            unsolved = False
common()#attack that works often and takes less than a second, should definitely be done first
dictionary(10000)#also short attack, guesses all one-word all-lowercase passwords
bruteForce("1234567890", 13245678)#number passwords are not very common but hey, it doesn't take long to grind through 13245678 attempts
bruteForce("aoeuidhtnspyfgcrlqjkxbmwvz1234567890", 10000000)#common password format
combo(99, 1000000)
bruteForce("aoeuidhtnspyfgcrlqjkxbmwvzAOEUIDHTNSPYFGCRLQJKXBMWVZ1234567890~!@#$%^&*()_+`-=[]\;',./{}|:\"<>?", 100000000)
dictioary(10000000)
          
