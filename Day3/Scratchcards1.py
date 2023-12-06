with open("games.txt") as f:
    totalPoints = 0
    for line in f:
        scratchVals = line[9:39].strip()
        matchVals = line[42:].strip()
        scratchList = scratchVals.split()
        matchList = matchVals.split()
        
        matches = []
        for val in scratchList:
            if val in matchList:
                matches.append(int(val))
        totalPoints += 2**(len(matches)-1) if matches else 0
    print(totalPoints)
