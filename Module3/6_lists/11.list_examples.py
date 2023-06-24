"""List Test"""
l1=[i for i in range(5)]
print(l1) #0,1,2,3,4

l2=[0 for j in range(5)]
print(l2)#0,0,0,0,0

l3=[2-k for k in range(5)]
print(l3)#2,1,0,-1,-2

l4=[3-l for l in range(-3,3)]
print(l4)#6,5,4,3,2,1

l5=[m+3 for m in range(-1,4)]
print(l5)#2,3,4,5,6

l6=[n-10 for n in range(-4,4,2)]
print(l6)#-14,-12,-10,8,

l7=[-2-l for l in range(-3,4)]
print(l7)#1,0,-1,-2,-3,-4,-5