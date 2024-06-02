class MathDojo:
    def __init__(self):
       self.result =0
    def add(self,*nums):              
     for num in nums:
        self.result+=num
     return self

    
    def subtract(self,*nums):    
     for num in nums:
        self.result-=num
     return self
    
md = MathDojo()
x = md.add(2).add(2,5,1).add(3,2,1).subtract(3,2).subtract(2,3).subtract(5,4).result
print(x)        