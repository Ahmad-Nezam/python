def CntPos(array):
    count = 0
    for i in array:
        if i >0:
            count+=1
            array[len(array)-1] = count
            return array     
print(CntPos([1,6,-4,-2,-7,-2]))

