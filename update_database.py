def updateCostumeDatabase(data):
    file = open("costumes.txt","w")
    for i in range(len(data)):
        file.write(f"{(data[i][0]).strip()}, {(data[i][1]).strip()}, {(data[i][2]).strip()}, {(data[i][3]).strip()}")
        if(i != len(data)-1):
            file.write("\n")