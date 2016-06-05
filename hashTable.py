'''
Hash-table in Python
Author: Sundip Desai

Class and Methods:
------------------

class myDict, method def__init__(self,SLOTS)
input: SLOTS = number of elements in dictionary
output: none

class myDict, method placeValue(self, key, value)
inputs: key = dictionary or hash table numeric key; value = associated value tied to key
outputs: none

class myDict, method getValue(self, key)
input: key = dictionary or hash table key
output: value tied to key

Version 1:
---------
Hash table is structured using a list containing tuples.
Tuples are key-value pair. Uses remainder method as hash function
to determine which slot tuple should go in. Collision prevention performed
by linear probing. If all slots are full in table, a prompt will be displayed
to user indicating hash table is full

'''

class myDict:
    def __init__(self, slots):
        if(slots <= 0):
            print('Invalid slot length!')
            return
        self.SLOTS = slots
        self.hash = [None]*self.SLOTS

    def  placeValue(self, key, value):
        if (not key):
            print('Empty key entry, try again!')
            return

        if(key%1 != 0): #Integer keys only
            print('Non-Integer key, try again!')
            return

        idx = key%self.SLOTS
        if self.hash[idx]: # Location is occupied, use linear probing
            for i, j in enumerate(self.hash):
                if(j == None):
                    self.hash[i] = tuple((key, value))
                    return
            print('No more slots available in hash table!')
            return
        else:
            self.hash[idx] = tuple((key,value))
        return

    def  getValue(self, key):
        idx = key%self.SLOTS
        if(self.hash[idx][0] == key):
            return self.hash[idx][1]
        else:
            for i in self.hash:
                if(i[0] == key):
                    return i[1]
            print('This key does not exist in the table!')



'''

Unit tests
----------
myHash = myDict(10)
myHash.placeValue(1,100)
myHash.placeValue(3,182)
myHash.placeValue(2,28)
myHash.placeValue(4,99)
myHash.placeValue(0,66)
myHash.placeValue(10,45)
myHash.placeValue(100,23)
myHash.placeValue(3,77)
myHash.placeValue(1.33,1)
myHash.placeValue(88,1)
myHash.placeValue(14,14)
myHash.placeValue(30,40)

print(myHash.getValue((10)))
print(myHash.getValue((17)))
print(myHash.hash)

'''



