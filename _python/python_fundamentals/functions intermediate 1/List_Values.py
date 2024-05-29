dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    print(len(dojo['locations']),'locations')
    for location in dojo['locations']:
        print(location) 
print()        

print(len(dojo['instructors']),'Instructors')
for instructors in dojo['instructors']:
    print(instructors) 

printInfo(dojo)

       
