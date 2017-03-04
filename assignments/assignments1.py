class CrossWord():
    def countWords(self, board, size):
        t = 0
        for slots in board:
            temp = slots.split("X")
            for empty in temp:
                k = empty.count(".")
                if(k==size and size >=2):
                    t=t+1
        return t

class Abacus:
    def add(self, original, val):
        y=[]
        z=[]
        for hyphen in original :
            y.append(str(9-hyphen.find('---')))
        s = map(str, str(int(''.join(y)) + val))
        for values in s:
            print values
            k=[]
            for j in range(0,10):
                if(j < 9 - int(values)):
                    k.append('o')
                elif(j == 9 - int(values)):
                    k.append('---')
                else:
                    k.append('o')
            z.append(''.join(map(str,k)))
        return tuple(z)


class WordFind():
    def findWords(self, grid, wordList):
        pass
    
class EventOrder():
    def getCount(self, longEvents, instantEvents):
        pass

