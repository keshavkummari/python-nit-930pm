#!/usr/bin/python

# tuple1, tuple2 = (123, 'xyz', 'minnu'), (456, 'abc')

tuple1=(123, 'xyz', 'minnu')
tuple2=(456, 'abc')

"""
print ("First tuple length : ", len(tuple1),type(tuple1))
print ("Second tuple length : ", len(tuple2))
"""
tuple1, tuple2 = ('123', 'xyz', 'minnu', 'abc'), (456, 700, 200)

print ("Min value element : ", min(tuple1))
print ("Max value element : ", max(tuple1))

print ("Min value element : ", min(tuple2))
print ("Max value element : ", max(tuple2))


aList = [123, 'xyz', 'minnu', 'abc']
aTuple = tuple(aList)

print ("Tuple elements : ",type(aTuple),aTuple)

print("Convert tuple into list",list(aTuple))
