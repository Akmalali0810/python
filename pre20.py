fileHandle = open("bca.txt","r")
tot = 0
vowels = ['a','e','i','o','u']

for char in fileHandle.read():
    if char in vowels:
        tot = tot+1

fileptr = open("bva.txt","r");
print(filter.read())
print("\ntotal vowels are:")
print(tot)