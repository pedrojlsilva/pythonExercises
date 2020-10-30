
class ContarCaracteres:
    def __init__(self, string):
        self.string=string
        self.stringLower = ""
        for i in string:
            if i.isalpha() :
                self.stringLower +=i.lower()
            elif i==" ":
                self.stringLower +=i
        

    def getWhiteSpace(self):
        count=0
        for i in self.string:
            if i == " ":
                count+=1
        
        return count

    def countA(self):
        count=0
        for i in self.string:
            if i == "a" or i == "A":
                count+=1

        return count

    def countPairs(self):
        maxCount=0
        finalPair=str()
        for j in range(len(self.stringLower)-1):
            
            substring = self.stringLower[j:j+2]
            if not (substring[0] == " " or substring[1] == " "):
                string_size = len(self.stringLower)
                substring_size = 2
                count = 0
                for i in range(0,string_size-substring_size+1):
                    if self.stringLower[i:i+substring_size] == substring:
                        count+=1

                if count > maxCount:
                    maxCount=count
                    finalPair=substring

        if maxCount == 0:
            return 'NENHUM PAR', 0

        return finalPair, maxCount


strInput=input()
while strInput != "NAO QUERO MAIS":
    frase=ContarCaracteres(strInput)

    print(frase.getWhiteSpace())
    print(frase.countA())
    par, counter = frase.countPairs()
    if counter>0:
        print(counter)

    print(par)
    
    strInput=input()

