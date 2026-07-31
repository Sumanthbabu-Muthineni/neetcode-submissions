class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        #creating_buckets

        buckets=[]
        for i in range(len(nums)+1):
            buckets.append([])

        #mapping repeated ones into buckets

        for ele in freq:
            count=freq[ele]
            buckets[count].append(ele)
        
        # result_list making
        output=[]

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                if len(output)==k:
                    return output
                output.append(num)
        return output


        