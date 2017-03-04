class AccountBalance:
    def processTransactions(self, startingBalance, transactions):
        x = 0
        y = 0
        for value in transactions:
                ret = value.split(" ")
                if(ret[0]== 'C'):
                    x = x + int(ret[1])
                else:
                    y = y + int(ret[1])
        return startingBalance+x-y

class AdditionGame():
    def getMaximumPoints(self, A, B, C, N):
        final_points = 0
        for number in range(0,N):
            x = max(A, B, C)
            final_points = final_points + x
            if(x == A):
                A = A-1
            elif(x == B):
                B = B-1
            else:
                C =C-1
            number = number+1
        return final_points

class ATaleOfThreeCities():
    def connect(self, ax, ay, bx, by, cx, cy):
        import math
        n1 = len(ax)
        n2 = len(bx)
        n3 = len(cx)
        temp1 = math.sqrt((ax[0]-bx[0])**2+(ay[0]-by[0])**2)
        for i in range(0, n1):
            for j in range(0, n2):
                if(temp1 > math.sqrt((ax[i]-bx[j])**2 + (ay[i]-by[j])**2)):
                    temp1 = math.sqrt((ax[i]-bx[j])**2 + (ay[i]-by[j])**2)
        temp2 = math.sqrt((ax[0]-cx[0])**2+(ay[0]-cy[0])**2)
        for i in range(0, n1):
            for j in range(0,n3):
                if(temp2 > math.sqrt((ax[i]-cx[j])**2+(ay[i]-cy[j])**2)):
                    temp2 = math.sqrt((ax[i]-cx[j])**2+(ay[i]-cy[j])**2)
        temp3 = math.sqrt((cx[0]-bx[0])**2+(cy[0]-by[0])**2)
        for i in range(0,n2):
            for j in range(0,n3):
                if(temp3 > math.sqrt((bx[i]-cx[j])**2+(by[i]-cy[j])**2)):
                    temp3 = math.sqrt((bx[i]-cx[j])**2+(by[i]-cy[j])**2)
        return round((temp1+temp2+temp3) - max(temp1,temp2,temp3), 10)

class IntoTheMatrix(object):
    def takePills(self, turns, N):
        ans = 0
        cur = 1
        while cur < N:
            ans += 1
            cur *= turns + 1
        return ans
    
    
