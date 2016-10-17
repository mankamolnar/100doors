#write out which doors are open
def writeOpenedDoors(allDoors):
    string = "Opened doors: "
    for i in range(0, len(allDoors)):
        if allDoors[i] == "o":
            string += str(i)+", "
    print(string)

#init
doors = ["c"] * 100

#magic :D
for i in range(1, 101):
    j = 0
    for value in doors:
        if (j % i == 0):
            if doors[j] == "c":
                doors[j] = "o"
            elif doors[j] == "o":
                doors[j] = "c"
        j += 1

#write out the opened doors
writeOpenedDoors(doors)