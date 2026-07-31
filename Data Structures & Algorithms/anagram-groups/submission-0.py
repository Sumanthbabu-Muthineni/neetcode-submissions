class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt=dict()
        for ele in strs:
            keyy="".join(sorted(ele))
            if keyy not in dictt:
                dictt[keyy]=[]
            dictt[keyy].append(ele)
        return list(dictt.values())
        

        