# palindrome number
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

# palindrom string
a = str(input("enter the name:"))
if a==a[::-1]:
    print("string is palindrom")
else:
    print("string is not palindrom")






