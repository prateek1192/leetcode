class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []
        if len(self.nums):
            self.sums.append(self.nums[0])
        for i in range(1,len(self.nums)):
            value = self.sums[i-1] + self.nums[i]
            self.sums.append(value) 
            

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #print (self.sums)
        if i==0:
            return self.sums[j]
        return self.sums[j]-self.sums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
