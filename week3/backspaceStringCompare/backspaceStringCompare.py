class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arrS = []
        arrT = []

        for i in s:
            if i != '#':
                arrS.append(i)
            else:
                if arrS:
                    arrS.pop()
        
        for i in t:
            if i != '#':
                arrT.append(i)
            else:
                if arrT:
                    arrT.pop()
        
        return arrS == arrT