# Update Values in Dictionaries and Lists
x = [[5,2,3] , [15,8,9]]

students1 =[   {'first name' : 'michael' , 'last name' : 'Bryant'},
{'first name':'john','last name':'Rosales'}]

sports_directory={'basketball':['kobe','jordan','james','curry'],
                  'soccer':['Andres','ronaldo','rooney'] }
z=[{'x':10 , 'y' : 30}]



# Iterate Through a List of Dictionaries

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'} ]




def iterateDictionary(students):
   
    for i in students:
    
                                                            
         print('first name -',i['first_name'],'last name -',i['last_name'])

print(iterateDictionary(students))         




