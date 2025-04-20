import random
Secret_number=random.randint(0,15)
count_guess=0
while count_guess<10:
    num=int(input("Guess:"))
    count_guess+=1
    if num==Secret_number:
        print("congrat")
        break
    if num>Secret_number:
        print("less than")
    else:
        print("bigger than")
