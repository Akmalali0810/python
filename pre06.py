num=int(input("enter the number:"))
sum = 0
temp = sum
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")