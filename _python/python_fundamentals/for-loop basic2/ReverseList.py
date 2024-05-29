def ReverseList(array):
    ReverseList=[]
    for i in range(0,len(array)):
     ReverseList.append(array[len(array)-1-i])
    return ReverseList    
print(ReverseList([1,2,3,4,5]))