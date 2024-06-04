class Animals:
    def __init__(self,name,age,health_lev,happy_lev):
        self.name =name
        self.age=age
        self.health_lev=health_lev
        self.happy_lev=happy_lev

    def display_info(self):
        print(f"name : ",self.name ,"Heath : ",self.health_lev, "Happiness: ",self.happy_lev)

    def feed(self):
        self.health_lev += 10
        self.happy_lev += 10

class Lion(Animals):
    def __init__(self, name, age=7, health_lev=5, happy_lev=10):
        super().__init__(name, age, health_lev, happy_lev)

    def feed(self):
        self.health_lev += 8
        self.happy_lev += 5    
class Tiger(Animals):
    def __init__(self, name, age=6, health_lev=20, happy_lev=15):
        super().__init__(name, age, health_lev, happy_lev)
    
    def feed(self):
        self.health_lev += 12
        self.happy_lev += 15

class Bear(Animals):
    def __init__(self, name, age=5, health_lev=25, happy_lev=35):
        super().__init__(name, age, health_lev, happy_lev)
    
    def feed(self):
        self.health_lev += 18
        self.happy_lev += 25
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def add_bear(self, name):
        self.animals.append(Bear(name))    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Baloo")
zoo1.print_all_info()
