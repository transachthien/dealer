from TiKiTarget import TikiTarget

def getTargetFromFile(fileName):
    targetFile = open(fileName, "r", encoding="utf8")
    lines = targetFile.readlines()
    targetFile.close()

    targets = []
    n = len(lines)
    i = 0

    while i < n:
        newTarget = TikiTarget(lines[i].strip(), lines[i+1].strip())
        targets.append(newTarget)
        i = i+2
    return targets