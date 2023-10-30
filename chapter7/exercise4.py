def mars_weight():
    numMembers = int(input("How many members in your family? "))
    totalWeight = 0
    for i in range(numMembers):
        member = int(input(f"Enter the Earth weight of family member {i+1}: "))
        member *= 0.3782
        totalWeight += member
    print(f"Your family's total weight would be {totalWeight} lbs!")

mars_weight()