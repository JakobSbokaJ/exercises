gList = ["Eren Bunul","Eren's mom","Eren's dad"]

for guest in gList:
    print(f"{guest}, please come to my dinner. It'll be quite fire.")

print("Sadly, Eren's mom cannot make it.")

gList[1] = "fedy fabear"

for guest in gList:
    print(f"{guest}, I am begging you to pull up to my dinner party. There will be water.")

print("A larger table has been found!")

gList.insert(0, "chika")
gList.insert(2, "bony")
gList.append("foksie")

for guest in gList:
    print(f"Hey {guest}, please - PLEASE - come to my dinner. It's at this diner in some small town with pizza I think.")

print("THE TABLE CAN'T SHIP IN TIME")

for i in range(len(gList)-2):
    person = gList.pop()
    print(f"Sorry {person}, you can't come.")

for guest in gList:
    print(f"Congrats {guest}, you can still pull up!")

del gList[0]
del gList[0]
print (gList)