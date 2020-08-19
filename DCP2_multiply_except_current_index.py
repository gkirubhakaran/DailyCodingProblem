#Daily coding problem 2
#Given a list - store the multiplication of all elements except the current index

mylist = [1,2,3,4,5]

for x in range(0,len(mylist)):
    temp = mylist[:x] + mylist[x+1:]
    result = 1
    for element in temp:         
        result = result * element
    resultset[x] = result
    print resultset
