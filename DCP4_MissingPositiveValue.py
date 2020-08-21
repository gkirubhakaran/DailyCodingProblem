def MissPosVal(mylist):     
    searchMin = 1
    for i in range(0,len(mylist)):     
       temp = searchMin                
       for j in range(0,len(mylist)):  
          if searchMin == mylist[j]:  
             searchMin+=1    
             break   
       if temp == searchMin:         
          break
    print searchMin 
 
 
 A = [ 3, 4, -1, 1 ]
 
 searchMin(A)
 
