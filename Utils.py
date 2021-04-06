def pyramid(ls):
    floorCount = 0
    numcount = 0
    order=0
    while numcount < len(ls):
        numcount += (floorCount) + 1
        floorCount += 1
    spaceCount = floorCount - 1
    for i in range(0, floorCount):
        for j in range(0, spaceCount):
            print(end=" ")
        spaceCount = spaceCount - 1
        for j in range(0, i + 1):
            try:
                print(str(ls[order])+" ", end="")
                order+=1
            except:
                print("*" + " ", end="")
        print("\r")
strx=""
with open("data.txt","r") as file:
    for line in file:
        strx+=line.replace("\n","")
pyramid(strx.split(","))
