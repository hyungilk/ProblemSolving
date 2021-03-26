class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums[0] == 1:
            cnt = 1
        else:
            cnt = 0
        if len(nums) == 1:
            return cnt
        cnt_list = []
        for i in range(1,len(nums)):
            if nums[i] == 1 and nums[i-1] == 1:
                cnt += 1
                cnt_list.append(cnt)
            elif nums[i] == 0 and nums[i-1] == 1:
                cnt_list.append(cnt)
                cnt = 0
            elif nums[i] == 1 and nums[i-1] == 0:
                cnt = 1
                cnt_list.append(cnt)
            else:
                cnt = 0
                cnt_list.append(cnt)
        return max(cnt_list)
                
