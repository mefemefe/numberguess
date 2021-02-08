import random
number = random.randrange(50)
tries = 3
while tries >0:
    guess = input("ENTER A NUMBER FROM 1 TO 50: ")
    try:
        if int(guess) == number:
            print("\nYOU WIN!!!")
            if tries == 3:
                print("FIRST TRY!!")
            elif tries == 2:
                print("SECOND TRY!")
            elif tries == 1:
                print("THIRD TRY")
            break
        else:
            print("NOPE")
            if number % 2 == 0:
                print("THE NUMBER IS EVEN")
            else:
                print("THE NUMBER IS ODD")
            if number > 25:
                print("NUMBER IS > 25")
            else:
                print("NUMBER IS LOWER THAN 26")
            if tries == 2:
                print("NUMBER ENDS IN "+str(number)[len(str(number))-1])
            tries -= 1
    except:
        print("NOT A NUMBER")
        continue
print("***    NUMBER WAS "+str(number)+"    ***")