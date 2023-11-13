def moon_weight(startWeight,increment,numYears):
    for i in range(1,numYears+1):
        weight2 = startWeight
        weight2 *= 0.165
        print(f"Year: {i} Weight: {weight2}")
        startWeight += increment

moon_weight(90,0.25,5)
moon_weight(30,0.25,20)
moon_weight(300,5,100)