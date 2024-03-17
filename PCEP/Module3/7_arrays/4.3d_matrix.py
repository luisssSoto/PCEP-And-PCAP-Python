"""Array's 4d"""
print("Welcome to Arrays 4d")
'''Imagine one hospital. It has 2 buildings,(adult center and child center respectevely) 
they have 10 floors each one and, 
there are 20 rooms in each floor and 6 beds in each room
So that, We need an array that it can get and process information about the beds that 
are available or not'''

hospital=[[[[beds for beds in range(6)]for rooms in range(20)]for floors in range(10)]for building in range(2)]
print(hospital)
print()

# Now you can give to Adolf patient who is a cardiology adult patient 
# the room 7 and the bed number 3
#Note:
#building 1= Adult center
#floor 6= Cardiology's floor
#room 7 = Adolf's room
#bed 3 = Adolf's bed

hospital[0][5][6][2]='Adolf\'s bed'
print(hospital)

'''The hospital directors decided to fix all the rooms, but this change 
needs to be slow, so that, they decided to fix the last bed for each room
so... you need to put all of them in "Not available"'''

for building in hospital:
    for floor in building:
        for room in floor:
            room[5]='Not available'
print(hospital)