string = input("Enter a string: ")
lst = []
frequency = []
for letter in string:
    lst.append(letter)
print(lst)
store=' '
counter=int(0)
for x in range(0,len(lst)):
    store=lst[x]
    counter=0
    for y in range(0,len(lst)):
        if store==lst[y]:
            counter+=1
    frequency.append(counter)
even=0
odd=0
for check in frequency:
    if check%2==0:
        even+=1
    elif check%2!=0:
        odd+=1
if even==len(frequency):
    print("Even = 0")
elif odd==len(frequency):
    print("Odd = 1")
else:
    print("Neither = 2")
print(frequency)