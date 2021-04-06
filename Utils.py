def pyramid(ls):
    floorCount = 0
    numcount = 0
    order=0
    while numcount != len(ls):
        numcount += (floorCount) + 1
        floorCount += 1
    spaceCount = floorCount - 1
    for i in range(0, floorCount):
        for j in range(0, spaceCount):
            print(end=" ")
        spaceCount = spaceCount - 1
        for j in range(0, i + 1):
            print(str(ls[order])+" ", end="")
            order+=1
        print("\r")
ls=[6,6,9,2,1,3,7,4,4,5]
pyramid(ls)
