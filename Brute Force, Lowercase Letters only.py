pw = input("Enter your password: ")
cracked = false #state of password cracking
chars = "qwertyuiopasdfghjklzxcvbnm" #all the characters the the program will try
charOn = [-1] #holds all the character values
attempts = 0
while not cracked:
    attempts += 1
    
    #changes the right-most character of the password that is being attempted
    charOn[len(charOn) - 1] += 1
    
    #if any character in charOn is over the limit (in this case, z), it switches it back to the beginning (a) and changes the previous character by 1
    for i in range(0, len(charOn)-1):
        if charOn[i] > len(chars):
            charOn[i] = 0
            charOn[i-1] += 1
            
    #if the first character is z, then change it back to a and add a new character
    if charOn[0] > 26: 
        charOn[0] = 0
        charOn.append(0)
        
    #the current password attempt
    attempt = ""
    
    #decodes charOn into a string and store it in attempt
    for i in range(0, len(charOn)-1):
        attempt += chars[charOn[i]]
    
    #check if we got the password
    if attempt == pw:
        print("Your password was found! It is " + attempt + ", right? It took me " + attempts + " attempts to find it.")
        unsolved = false
