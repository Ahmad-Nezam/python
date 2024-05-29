def bigsiz(array):
    for i in range(len(array)):
        if array[i]>0:
            array[i]='BIG'
    return array
print(bigsiz([-1,3,5,-5]))            

   
