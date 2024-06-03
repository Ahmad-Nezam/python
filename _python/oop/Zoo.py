class Zoo:
    def __init__(self,zoo_name):
        self.animals =[]
        self.name=zoo_name
    def add_lion(self,name):
        self.animals.append('Lion',(name))
    def add_tiger(self,name):
        self.animals.append('Tiger',(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 =Zoo('ahmad zoo')          
zoo1.add_lion('ahmad')
zoo1.add_lion()
zoo1.add_tiger()
zoo1.add_tiger()
zoo1.print_all_info()