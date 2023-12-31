'''Remember at first we need to add positional arguments'''
def areaTriangle(b,h,form=2):
    result = b * h / 2
    return result

res = areaTriangle(5, h=10)
print(res)


'''Remember None:
You can uncomment the line 16 and the error will be the same'''
def animalsOfFarm(animalFarm):
    match animalFarm:
        case "horse":
            return "caballo"
        case "cow":
            return "vaca"
        # case _:
        #     return None

print(animalsOfFarm("horse"))
print(animalsOfFarm("cow"))
print(animalsOfFarm("camel"))
