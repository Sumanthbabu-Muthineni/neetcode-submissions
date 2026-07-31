class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_Set=set(nums)
        longg=0
        for num in nums:
            if num-1 not in hash_Set:
                cur_len=1
                cur_num=num
                while cur_num+1 in hash_Set:
                    cur_len+=1
                    cur_num+=1
                longg=max(longg,cur_len)
        return longg

        