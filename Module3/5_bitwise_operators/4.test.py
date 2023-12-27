print('Test bitwise operators')
x=0b1000_0001
y=0b10
print(x & y) #0000_0000 ->0
print(x | y) #1000_0011 ->131
print(~ x) #0111_1110 -> -130
print(x ^ 129) #1000_0011 ->131
print(x >> 3) #0001_0000 -> 16
print(x << 3) #1000_0001_000 -> 1032
