#Daily coding problem 1
#Given a list and a value k - return which two elements will add up to k


mylist = [10, 15, 3, 7]
k = 17

diff = []
for x in mylist:
   if x in diff:
      print x, k-x , " are a pair"
   diff.append(k-x)
