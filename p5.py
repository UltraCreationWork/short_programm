# find the count of element in list and gives output {"element":"number of count"}
#way 1
from collections import Counter
c = Counter([1,52,4,1,5,8,6,4,5])
print(c)

# way 2
output = dict()
a = [1,2,1,4,4,1,5,4,1,6,1,5,1,8,4,1,1,6,5,1,5,4,6,1]
for i in a:
    output[i] = a.count(i)
print(output)


