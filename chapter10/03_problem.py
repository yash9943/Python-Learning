''' Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute? '''

# Not Change the class attributes

class abc:
    a = 4
    
o = abc()
print(o.a) #print class attribute

o.a = 0
print(o.a) #print instance attribute

print(abc.a) #print class attribute