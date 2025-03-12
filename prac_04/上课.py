names=["Ada","Alan","Bill","John"]
print(",".join(names))
name_to_remove=input("who do you want to remove? ")
while name_to_remove!="":
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(",".join(names))
    else:
        print(f"{name_to_remove} is not in the list")
        name_to_remove=input( "who do you want to remove? ")