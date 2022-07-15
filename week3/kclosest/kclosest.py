import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = set()
        hm = {}

        for i in points:
            res = math.sqrt(i[0]**2 + i[1]**2)
            arr.add(res)
            if res in hm:
                hm[res].append(i)
            else:
                hm[res] = [i]

        arr = sorted(arr)

        resArr = []
        while arr:
            val = arr.pop(0)
            resArr += hm[val]

        return resArr[:k]