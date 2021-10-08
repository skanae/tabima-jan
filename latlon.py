from geopy.distance import geodesic
# (緯度, 経度)

def getlatlon(message):

    trimMessage = message.split() 
    # trimMessage = ["/tabi", "s100", "e100"]
    
    latOrder = trimMessage[1]
    lonOrder = trimMessage[2]
    # latdis = "s100"
    # londis = "e100"

    temp = binarySearch(KyotoStation,latOrder)
    destination = binarySearch(temp,lonOrder)

    latlon = [destination[0],destination[1]]
    return latlon

def binarySearch(startPoint,order):
    direction = order[0]
    lenOrder = int(order[1:])

    longest = [startPoint[0],startPoint[1]]

    if(direction == "n"):
        longest[0] = 46.0000
    elif(direction == "e"):
        longest[1] = 153.0000
    elif(direction == "s"):
        longest[0] = 24.0000
    elif(direction == "w"):
        longest[1] = 122.0000

    outer = longest
    inner = startPoint
    error = 1e10
    # print(outer,inner,error)
    while(abs(error) > 1):
        tmp=((inner[0]+outer[0])/2,(inner[1]+outer[1])/2)
        dis = geodesic(startPoint, tmp).km
        error = dis - lenOrder
        if(error>0):
            outer = tmp
        else:
            inner = tmp
        # print(tmp)
    destination=[tmp[0],tmp[1]]
    return destination

KyotoStation = [34.98625332246909, 135.7589705460798]

mes = "/tabi s50 e50"
latlon = getlatlon(mes)

print(latlon)

