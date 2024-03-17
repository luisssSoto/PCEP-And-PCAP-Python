"Who was George Boole"
print("Welcome to Boolean Literals")
print('Thanks George Boole for "Algebra Booleana"')
print(True == 1)
print(False == 0, "\n")

#Saving the literal in a variable
pigsCanFly=False
print(pigsCanFly)
mexicanFoodIsDelicious=True
print(mexicanFoodIsDelicious)

#Check the type of data
print(type(pigsCanFly))

#All the literal different to 0 and None will be True look at this 
intLiteralZero=bool(0)
noneLiteral=bool(None)
intLiteralNoZero=bool(25)
floatLiteral=bool(85.8)
strLiteral=bool('String')
lst=bool([1,2,3])
tup=bool((8.9,99.1,))
dic=bool({'fish': 'pez', 'whale': 'ballena'})

print(intLiteralZero,noneLiteral,sep='\t')
print(intLiteralNoZero,floatLiteral,strLiteral,lst,tup,dic,sep='\t')
print()

#The scenario above is only when you cast the literals
#but always when you compare them between True or False
#the only literals which will be equal to True or False,
#will be 1 and 0 respectively
print(True == 1)
print(True == 40)
print(True == 'Happy')
print(True == 3.4)
print(True == None)
print()
print(False == 0)
print(False == 4)
print(False == 'Sad')
print(False == 4.5)
print(False == None)