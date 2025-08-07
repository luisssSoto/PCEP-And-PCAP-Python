"""Section Test"""

# 1. 
print(len("""
"""))
print()

# 2. 
y = "yesteryears"
a_list = list(y)
print(a_list[3:6])
print()

# 3. 
for ch in "abc":
    print(chr(ord(ch) + 1), end="")