pws = open(PASSWORDFILEHERE.txt).split()
pw = input("Enter your password: ")
for i in range(0, len(pws)):
    if pws[i] == pw:
        print("Your password \"" + pws[i] + "\" has been found. It was number " + str(i + 1) + " on the most common password list.")