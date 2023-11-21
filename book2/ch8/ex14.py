def getCarInfo(manufacturer,model,color="",heated=""):
    info = {"manufacturer":manufacturer,"model":model}
    if color:
        info["color"] = color
    if heated:
        info["heated"] = heated
    return info

carInfo = getCarInfo("Honda","Accord","blue","yes")
car2Info = getCarInfo("Ford","F150")

print(carInfo)
print(car2Info)