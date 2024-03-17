''' Operator's Hierarchy and then left link'''

print("This is hierarchy:", 1 - 3 *2 **2)
print("This is left link:", 10/2/5)
print("but there is an exception... with the exponent:")
print(2**3**2, 'the last result was because we used a rigth link')
print("Remember all inside parentheses have greatest hierarchy:", (5 * ((25 % 13) + 100) / (2 * 13)) // 2)

"""I show you the complete hierarchy in Pyhon"""

'''Hierarchy
1. parentheses ()
2. ! ~ (type) ++ -- + -   Unary
3. **
4. * / % 
5. + -                    Binary
6. << >> 
7. <<=>> = 
8. == != 
9. &
10. |
11. &&
12. ||
13. = += -= *= /= %= &= ^= |= >>= <<=
'''