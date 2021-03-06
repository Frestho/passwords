import math
charOn = []
mode = -1
while not (mode == "" or mode == "0" or mode == "1"):
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
    attempts += charOn[i]*(len(chars)**(len(charOn) - i - 1)) + 1
print("It would take " + str(attempts) + " attempts for your password to be cracked.")
benchmark = input("To calculate how much time it would take for your password to be cracked, run my original brute force cracking program for about a minute and check the value of the attempts variable. Enter its value here: ")
print("It would take " + str(round(int(benchmark) * 60 * attempts, 2)) + " seconds for your password to be cracked. This is only an approximation.")
print("It would take " + str(math.floor((int(benchmark) * 60 * attempts) / 86400)) + " days, " + str(math.floor((int(benchmark) * 60 * attempts) % 86400 / 3600)) + "hours, " + str(math.floor((int(benchmark) * 60 * attempts) % 3600 / 60)) + " minutes, and " + str(round((int(benchmark) * 60 * attempts) % 60, 2)) + " seconds for your password to be cracked. This is only an approximation.")
