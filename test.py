import random
def randGame():
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
for i in range(1,11):
    print(i)
# randGame()

