# a=[3,5,7]
# number = int(input("Enter a number: "))
# print(number in a)

# The code above checks if the number entered by the user is in the list 'a'.

# print(1 in range(5))

# The code above checks if the number 1 is in the range from 0 to 4 (inclusive).

# w=[4,10]
# e=[5,6]
# print(w*4)

# The code above multiplies the list 'w' by 4, resulting in a new list that contains the elements of 'w' repeated 4 times.

s=[1,2,3,17,20]
# print(s[1:4])
# print(s[-2])
# print(s[:])
# s.append([50,10])
# print(s)
# s.extend([100,200])
# s.sort(reverse=True)
# print(s)
# del s[1]
# print(s)

# The code above deletes the element at index 1 from the list 's' and prints the updated list.

h=dict()
h["syria"]=2024
m={"egypt":1000,"syria":2000}
m["iraq"]=3000
print(m)

print(1000 in m.values())

for key,value in m.items():
    print(key)
    print(value)