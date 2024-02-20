print("Options: 1, 2 3, 4, 5, 6, 7, 8, 9, 10")
run = input ("Enter the problem you want to run: ")
run = int(run)

# 1. Write a program that prints out the numbers 1 to 1000. (+5 points)
if run == 1: 
    print ("Running Problem 1")
    for count in range (1,1001): 
        print (count)

# 2. Write a program that prints out the odd numbers between 1 and 1000. (+5 points)
elif run ==2: 
    print ("Running Problem 2")
    for count in range (1,1001, 2):
        print (count)

# 3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. 
elif run == 3: 
    print ("Running Problem 3")
    for count in range (1,1001):
        if count  % 3 == 0: 
            print (count)

# 4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5.
elif run == 4: 
    print ("Running Problem 4")
    for count in range (1,1001): 
        if count % 3 == 0 or count % 5 == 0: 
            print (count)

# 5. Write a program that asks the user to enter a number and prints out all the numbers 
    # between 1 and that number that are divisible by 11 or 13. The number entered should be 
    # greater than 200. (+10 points) Extra credit if the programs asks again if the number is 
    # less than 200. (+5 points)
elif run ==5: 
    print ("Running Problem 5")
    count = int(input ("Enter a number: "))
    
    while count <=200:
        print ("Enter a new number; one that is greater than 200.")
        count = int(input ("Enter a number: "))
    
    while count > 200: 
        for count in range (1,count):
            if count % 11 == 0 or count % 13 == 0: 
                print (count) 

# 6. Write a program that prints out each letter of a string line by line (+5 points)
elif run == 6: 
    print ("Running Problem 6")
    string = input ("Enter word (s) or statements: ")
    for letters in string: 
        print (letters) 

# 7. Write a program that asks the user to enter a string and outputs every second letter. 
    #   The string must be more than 10 letters long. (+10 points)
elif run == 7: 
    print ("Running Problem 7")
    string = input ("Enter a string with more than 10 letters: ") 
    if len(string) < 10: 
        print ("Enter a new string with 10 or more letters.")
    else: 
        printing = string[1::2]
        for letter in printing:
            print (letter)
        


# 8. Write a program that rolls 1000 dice and prints out the number of times each number was 
    # rolled. (+15 points)
elif run == 8: 
    print ("Running Problem 8")
    import random 
    ones = 0 
    twos = 0 
    threes = 0 
    fours = 0 
    fives = 0 
    sixes = 0 
    for rolls in range (10001):
        dice = random.randint(1,6)
        if (dice == 1): 
            ones +=1
        elif (dice == 2):
            twos +=1
        elif (dice == 3):
            threes +=1
        elif (dice == 4):
            fours +=1
        elif (dice == 5):
            fives +=1 
        else: 
            sixes +=1
        print (dice)
    print (f"After 1000 rolls, we rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s.")

# 9. Write a program that checks if a given number is a prime number. A prime number is a 
    # number that is only divisible by 1 and itself. The user enters a number and the programs 
    # prints out whether the number is a prime number or not. (+15 points)
    # prime numbers include: 1, 3, 5, 7, ... 
elif run == 9: 
    print ("Running Problem 9")
    num = int(input ("Enter a number: "))
    prime = True 

    for i in range (2, num+1): 
        if num % i == 0 and num != i: 
            prime = False 
            print (f"{num} is not a prime number.")
            break
    if num ==1:  
        print (f"{num} is not a prime number!")
    elif num ==2: 
        print (f"{num} is a prime number!")
    elif prime == True:
        print (f"{num} is a prime number!")

# 10. Write a program that prints out the prime numbers less than 1000. (+20 points)
elif run == 10: 
    print ("Running Problem 10")
    prime = True 
    for count in range (2,1001):
        prime = True 
        for i in range (2, count+1): 
            if count % i == 0 and count != i: 
                prime = False 
                break
            
        if prime == True: 
            print (count)

