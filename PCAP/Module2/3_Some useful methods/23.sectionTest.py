# 1. capitalize()
immutable = "immutable str"
print(immutable.capitalize())
print(immutable)
immutable = immutable.capitalize()
print(immutable)
print()

# 2. center()
print("[" + "center".center(len("center"))+ "]")
print("[" + "center".center(8)+ "]")
print("[" + "center".center(7, "¡") + "!" +  "]")
print()

# 3. endswith()
print("pangolin".endswith("lin"))
print("pangolin".endswith("li"))
print()

# 4. find() is more secure than index()
print("Alligator".find("l"))
print("Alligator".find("l", 2))
print("Alligator".find("l", 2, 2))
text = """Bacon ipsum dolor amet short ribs brisket venison rump drumstick pig 
sausage prosciutto chicken spare ribs salami picanha doner. Kevin capicola sausage, 
buffalo bresaola venison turkey shoulder picanha ham pork tri-tip meatball meatloaf 
ribeye. Doner spare ribs andouille bacon sausage. Ground round jerky brisket 
pastrami shank.
Pancetta tenderloin short loin sausage. Short loin shank prosciutto brisket, jerky 
ribeye cupim. Biltong prosciutto venison shank, corned beef bacon chicken spare 
ribs fatback tail pig sirloin chuck salami. Andouille beef ribs capicola alcatra 
bresaola flank.
Pastrami landjaeger pancetta shoulder t-bone, salami short loin. Ground round kevin 
ribeye venison swine buffalo kielbasa corned beef sausage. Beef biltong tail 
leberkas picanha boudin hamburger andouille prosciutto cow. Strip steak sirloin 
hamburger spare ribs picanha pork chop meatball chicken buffalo beef swine. 
Sirloin chicken fatback, bresaola drumstick cow frankfurter salami spare ribs 
t-bone filet mignon ground round pork belly meatball buffalo."""

index = text.find("bacon")
while index != -1:
    print(index, end="|")
    index = text.find("bacon", index + 1)
print()

# 5. isalnum()
print("Characters".isalnum())
print("1243".isalnum())
print("numb3r5And5tr1ng5".isalnum())

print(" ".isalnum())
print("".isalnum())
print("%".isalnum())
print()

# 6. isalpha()
print("is alpha".isalpha())
print("15 41ph4".isalpha())
print()

# 7. isdigit()
print("15 45".isdigit())
print("523333".isdigit())
print()

# 8. islower()
print("islower()")
print("mom dad".islower())
print("Mom".islower())
print()

# 9. isspace()
print("only spaces".isspace())
print("\t".isspace())
print("\n".isspace())
print("   ".isspace())
print()

# 10. isupper()
print("isupper()")
print("Upper".isupper())
print("upper".isupper())
print("UPPER".isupper())
print("UPPER ".isupper())
print()

# 11. join()
print("join()")
print(",".join([str(x) for x in range(5)]))
print("".join(["python", "3"]))
print()

# 12. lower()
print("LOW3R".lower())
print()

# 13. lstrip()
print("[" + "\t  lstrip method".lstrip())
print("www.linkedin.com".lstrip("www."))
# Note: The chars argument is not a prefix; rather, all combinations of its values are stripped:
print("www.linkedin.com".lstrip("nilwzke."))
print()

# 14. replace()
print("my favorite color is Yellow".replace("y", "i"))
print("Hello".replace("l", ""))
print("Hello".replace("l", "", 1))
print("World".replace("", "Mundo"))
print()

# 15. rfind()
print("py py".rfind("py"))
print("py py py".rfind("py", 5))
print("py py py".rfind("py", 2, 1))
print()

# 16. rstrip()
print("python.con".rstrip("conth"))
print("python.con".rstrip(".con"))
print("python    ".rstrip() + "]")
print()

# 27. split()
print("Guido Van Rossum".split())
print(" ".split())
print()

# 28. startswith()
print("Texas".startswith("Tex"))
print("Texas".startswith("ex"))
print()

# 29. strip()
print("[" + "   method strip    ".strip() + "]")
print("www.some.com".strip("omsecw"))
print()

# 30. swapcase()
print("UPPER & lower".swapcase())
print()

# 31. title()
print("the lORD OF thE ringS".title())
print()

# 32. upper()
print("uppercase".upper())
