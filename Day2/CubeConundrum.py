validGames = []


def getNumColorCubes(color):
    value = color.strip()
    digit = True
    i = 0
    while digit:
        if value[i].isdigit():
            i += 1
        else:
            digit = False
    return value[:i]

with open('games.txt') as f:
    for line in f:
        gameIndex = line.find(':')
        newLine = line[gameIndex+1:]
        sets = newLine.split(';')
        validGame = True

        for s in sets:
            value = s.strip()
            colors = value.split(',')
            for color in colors:
                numColorCube = int(getNumColorCubes(color))
                if 'green' in color and numColorCube > 13:
                    validGame = False
                elif 'red' in color and numColorCube > 12:
                    validGame = False
                elif 'blue' in color and numColorCube > 14:
                    validGame = False
        if validGame:
            validGames.append(int(line[4:gameIndex].strip()))
print(sum(validGames))
        
