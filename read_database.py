def readCostumesDatabase():
    data = []

    file = open("costumes.txt","r")
    line_data = file.readlines()
    for line in line_data:
        data.append(line.split(", "))
    file.close()
        
    return data