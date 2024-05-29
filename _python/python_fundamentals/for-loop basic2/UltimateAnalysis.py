def UltimateAnalysis(arr):
    dic = {'mini': arr[0],'maxi': arr[0],'totatl':0,'avg':0 ,'length':0 }
    for i in arr:
        if dic['maxi'] <i:
            dic['maxi']=i
        if dic['mini'] > i:
            dic['mini']=i
        dic['totatl'] +=i
        dic['avg'] += i/len(arr)
        dic['length'] = len(arr)       
    return dic
print(UltimateAnalysis([1,2,3,4,5,6]))  
             
        