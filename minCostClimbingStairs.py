class Solution:
    def __init__(self):
        self.minCost=[]


    def minCostClimbingStairs(self,cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.minCost.append(0)
        self.minCost.append(0)
        for i in range(2,len(cost)+1):
            if i==2:
                self.minCost.append(min(cost[i-1], cost[i-2]))
            elif i==3:
                self.minCost.append(min(self.minCost[i-1]+cost[i-1], cost[i-2]))
            else:
                value = min(self.minCost[i-1]+cost[i-1], self.minCost[i-2]+cost[i-2])
                self.minCost.append(value)
        #return (self.minCost)
        return self.minCost[-1]

