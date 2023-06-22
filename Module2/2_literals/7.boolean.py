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

print(intLiteralZero,noneLiteral,sep='\t')
print(intLiteralNoZero,floatLiteral,strLiteral,sep='\t')