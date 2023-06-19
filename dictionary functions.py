teachers = {"Dimple":"comp sc","pareet":"sociology"}
for key in teachers:
    print(key,str(teachers[key]))
teachers["New"] = "history"         #adding new elements
print(teachers)
print(teachers["Dimple"])           #printing particular value
teachers["Dimple"] = "2000"         #updating elements
print(teachers)
dict.pop("2000")         #to pop element
