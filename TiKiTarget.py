class TikiTarget:
    def __init__(self, patternStr="",categoryStr=""):
        self.patternString = patternStr
        self.patterns = self.__splitPattern()
        self.categoryUrl = categoryStr

    def info(sefl):
        return "patterns: " +sefl.patternString +" | category: " + sefl.categoryUrl + "|" + str(sefl.patterns)    

    def __splitPattern(sefl):
        newList = sefl.patternString.split(",")
        i = 0
        while i <len(newList):
            newList[i] = newList[i].strip()
            i = i + 1

        return newList     

    def getKeyWord(sefl):
        keyword=""
        for key in sefl.patterns:
            keyword = keyword + " "+key

        return keyword    
    def getSearchLink(sefl,pageNum):
        return sefl.categoryUrl+"?q="+sefl.getKeyWord()+"&ref=categorySearch&page="+str(pageNum)
