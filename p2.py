# find small length of strig in list
a = ["ishwar","karan","hello","new","is","a"]
min_count = min(len(i) for i in a)
for i in a: 
    if len(i)==min_count: print("small sting in list",i)

# find max length of string
max_count = max(len(i) for i in a)
for i in a:
    if len(i)==max_count: print("big lenght of string in list",i)


# another way
small_string = min(a,key=len)
long_string = max(a,key=len)
print("small sting in list",small_string)
print("big lenght of string in list",long_string)



    