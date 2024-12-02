from csvLoader import CsvLoader

# Edit these values:
profession = 'cook'   
lvl = 1.5
xprating = 0 #only gives accurate results for xprating 0 and 65 (xpscroll)

#######

def xpTable(level: int) -> int: 
    if level == 1: return 0
    if level == 2: return 1600
    if level == 3: return 3600
    if level == 4: return 6400
    if level == 5: return 10000
    if level == 6: return 14400
    if level == 7: return 19600
    if level == 8: return 25600
    if level == 9: return 32400
    if level == 10: return 40000 

def getXpFromLevel(level: float) -> float:
    lower = xpTable(int(level))
    upper = xpTable(int(level) + 1)
    return lower + (upper - lower) * (level - int(level))

# this function is not accurate, needs more data
def getXpRatingModifier(xprating: int) -> float:
    return 1 + xprating / 325

def getQuantity(loader: CsvLoader, profession, lvl):
    base = loader.getQuant(profession)
    if base is None: return None
    base = float(base)
    xp = getXpFromLevel(lvl)
    completedShare = xp / 40000
    modifier = getXpRatingModifier(xprating)
    return int( (base - base * completedShare)/modifier)





if __name__ == "__main__":
    primaryRessources = CsvLoader('primary.csv')
    secondaryRessources = CsvLoader('secondary.csv')    

    primaryQuantity = getQuantity(primaryRessources, profession, lvl)
    primaryType = primaryRessources.getType(profession)
    secondaryQuantity = getQuantity(secondaryRessources, profession, lvl)
    secondaryType = secondaryRessources.getType(profession)

    if secondaryQuantity != None:
        print(f"Primary: {primaryQuantity} {primaryType}")
        print(f"Secondary: {secondaryQuantity} {secondaryType}")
    else:
        print(f"Primary: {primaryQuantity} {primaryType}")