import time
words = open(words.txt).split()
wordOn = [-1]
pw = input("Enter your password: ")
start = time.time()
#adds numbers if the bare dictionary attack isn't working
number = []
attempts = 0
unsolved = true
while unsolved:
    wordOn[len(wordOn) - 1] += 1
    """
    for i in reversed(range(1, len(wordOn)):
        if wordOn[i] > len(words):
            wordOn[i] = 0
            wordOn[i - 1] += 1
    """
    #adds another item to the end of the word list if the first word is "overflowed"
    if wordOn[0] > len(words):
        wordOn[0] = 0
        numbers.append(-1)
    numbers[len(numbers)-1] += 1
    attempt = ""
    for i in range (0, len(wordOn)):
        attempt += wordOn[i]
    attempt += str(number[0])
    if attempt == pw:
        print("Your password \"" + attempt + "\" has been found! It took " + str(attempts) + " attempts and " + round(time.time() - start, 2) + " seconds to find your password."
