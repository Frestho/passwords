import math
charOn = []
mode = -1
while not (mode == "" or mode == "0" or mode == "1" or mode == "2"):
    mode = input("Select the mode you want to test. Nothing for all lowercase, 0 for numbers, 1 for all case letters + numbers, and 2 for all characters: ")
    if mode == "":
        chars = "aoeuidhtnspyfgcrlqjkxbmwvz"
    if mode == "0":
        chars = "1234567890"
    if mode == "1":
        chars = "aoeuidhtnspyfgcrlqjkxbmwvzAOEUIDHTNSPYFGCRLQJKXBMWVZ1234567890"
    if mode == "2":
        chars = "aoeuidhtnspyfgcrlqjkxbmwvzAOEUIDHTNSPYFGCRLQJKXBMWVZ1234567890~!@#$%^&*()_+`-=[]\;',./{}|:\"<>?"
pw = input("Enter your password here: ")
attempts = 0

#encode
for i in range(0, len(pw)):
    charOn.append(chars.index(pw[i]))

#decode
for i in range(0, len(charOn)):
    attempts += (charOn[i] + 1) * (len(chars) ** (len(charOn) - i - 1))
print("It would take " + str(attempts) + " attempts for your password to be cracked.")
benchmark = input("To calculate how much time it would take for your password to be cracked, run my original brute force cracking program for about a minute and check the value of the attempts variable. Enter its value here: ")
print("It would take " + str(round(60 / int(benchmark) * attempts, 2)) + " seconds for your password to be cracked. This is only an approximation.")
