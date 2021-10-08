from geopy.distance import geodesic
# (緯度, 経度)

KyotoStation = (34.98625332246909, 135.7589705460798)
input = ("n",100)

nowPlace = [34.98625332246909, 135.7589705460798]
longest = [34.98625332246909, 135.7589705460798]

if(input[0] == "n"):
    longest[0] = 46.0000
elif(input[0] == "e"):
    longest[1] = 153.0000
elif(input[0] == "s"):
    longest[0] = 24.0000
elif(input[0] == "w"):
    longest[1] = 122.0000

# outer = [(nowPlace[0]-longest[0])/2,(nowPlace[1]-longest[1])/2] 
# inner = nowPlace
# outest = longest
# innest = nowPlace
outer = longest
inner = nowPlace
# dis = geodesic(nowPlace, outer).km
# error = dis - input[1]

# tmp=((inner[0]+outer[0])/2,(inner[1]+outer[1])/2)
# dis = geodesic(KyotoStation, tmp).km
# print(dis)
error = 1e10

print(outer,inner,error)

while(abs(error) > 1):
    tmp=((inner[0]+outer[0])/2,(inner[1]+outer[1])/2)
    dis = geodesic(nowPlace, tmp).km
    error = dis - input[1]
    if(error>0):
        outer = tmp
    else:
        inner = tmp
    print(dis,tmp,inner,outer)
print(error,"\n",dis,"\n",tmp,nowPlace)
print("ここにとべ!",tmp)

# message=/tabi s100 e100
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

    longest = startPoint

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
    while(abs(error) > 1):
        tmp=((inner[0]+outer[0])/2,(inner[1]+outer[1])/2)
        dis = geodesic(nowPlace, tmp).km
        error = dis - lenOrder
        if(error>0):
            outer = tmp
        else:
            inner = tmp

    destination=[tmp[0],tmp[1]]
    retrun destination