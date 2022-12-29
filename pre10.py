num = int(input ("enter the a value="))
temp = num
rev = 0

while(num > 0):
    dig=num % 10
    rev=rev * 10 + dig
    num=num // 10

if(temp == rev):
    print("this value is palindrom number")
else:
    print("this value is not a palindorm number")
