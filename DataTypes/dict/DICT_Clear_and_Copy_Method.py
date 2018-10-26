#!/usr/bin/python
"""
ronnie = {'Name': 'minnu', 'Age': 7}

print("Student name is {0} and his age is {1}" .format(ronnie['Name'],ronnie['Age']))
print("Student name is {0} and his age is {1}" .format("Naresh",7))
print ("Length : %d" % len(ronnie)) # len() is function
print("FirstName: %s MiddleName: %s LastName: %s Age: %d" %('Guido','Van','Rossum',58))

dict_1 = {'Name':'minnu','Age':7}
print ("Equivalent String : %s" % str(dict_1))  # str() is function

dict_2 = {'Name': 'minnu', 'Age': 7}
print ("Variable Type : %s" % type(dict_2)) # type() is function

dict_3 = {'Name': 'minnu', 'Age': 7};

print ("Start Len : %d" % len(dict_3))
"""
d1 ={"FirstName":'Guido',"MiddleName":'Van',"LastName":'Rossum','Age':58}

print(d1,type(d1),id(d1),len(d1),dict(enumerate(d1)))

#d1.clear()   # clear() is method

print(d1,type(d1),id(d1),len(d1),dict(enumerate(d1)))

d2 = d1.copy() # copy() is method

print(d2,type(d2),id(d2),len(d2),dict(enumerate(d2)))
