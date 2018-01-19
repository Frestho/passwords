charOn = []
mode = input("Select the mode you want to test. Nothing for all lowercase, 0 for all case letters + numbers, and 1 for all characters: ")
if mode == "":
    chars = "qwertyuiopasdfghjklzxcvbnm"
if mode == "0":
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
if mode == "1":
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890~!@#$%^&*()_+`-=[]\;',./{}|:\"<>?"
pw = input("Enter your password here: ")
attempts = 0

#encode
for i in range(0, len(pw)):
    charOn.append(chars.index(pw[i]))

#decode
for i in range(0, len(charOn)):
    attempts += charOn[i]*(len(chars)**len(charOn)-i)
print("It would take " + str(attempts) + " attempts for your password to be cracked.")
benchmark = input("To calculate how much time it would take for your password to be cracked, run my original brute force cracking program for about a minute and check the value of the attempts variable. Enter its value here: ")
print("It would take " + str(int(benchmark) / 60 / attempts) + " seconds for your password to be cracked. This is only an approximation.")
