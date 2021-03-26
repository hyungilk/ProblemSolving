class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = []
        for num in nums:
            sq_nums.append(num ** 2)
        sq_nums.sort()
        return sq_nums
