def Avg(arr):
    sum =0
    for i in arr:
        sum+=i/len(arr)
    return sum
print(Avg([1,2,3,4]))