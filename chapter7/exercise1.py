def moon_weight(startWeight,increment):
    for i in range(1,15):
        weight2 = startWeight
        weight2 *= 0.165
        print(f"Year: {i} Weight: {weight2}")
        startWeight += increment

moon_weight(100,1)
moon_weight(30,0.25)
moon_weight(300,5)