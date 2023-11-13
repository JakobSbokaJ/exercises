def moon_weight():
    startWeight = input("Please enter your current Earth weight ")
    increment = input("Please enter the amount your weight might increase each year ")
    numYears = input("Please enter the number of years ")
    startWeight = int(startWeight)
    increment = int(increment)
    numYears = int(numYears)
    for i in range(1,numYears+1):
        weight2 = startWeight
        weight2 *= 0.165
        print(f"Year: {i} Weight: {weight2}")
        startWeight += increment

moon_weight()