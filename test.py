import random
rightNumber = random.randint(1,50)
while True:
    number = int(input("enter number: "))
    if rightNumber>number:
        print("bigger")
    elif rightNumber<number:
        print("smaller")
    else:
        break
print("right")

