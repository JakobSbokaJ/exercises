def getCarInfo(manufacturer, model, **extraInfo):
    info = {"manufacturer":manufacturer,"model":model}
    for key, value in extraInfo.items():
        info[key] = value
    return info

carInfo = getCarInfo("Honda","Accord",color="blue",heated="yes")
car2Info = getCarInfo("Ford","F150")

print(carInfo)
print(car2Info)