class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = {}
        for i, n in enumerate(nums):
            if n in c:
                c[n].append(i)
            else:
                c[n] = [i]
        M = max([len(i) for i in c.values()])
        return min([i[-1]-i[0] for i in c.values() if len(i) == M]) + 1
