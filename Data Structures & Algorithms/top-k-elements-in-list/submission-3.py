class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lst = []
        # from collections import defaultdict
        # cnt = defaultdict(int)
        # for n in nums:
        #     cnt[n]+=1
        # return list(dict(sorted(cnt.items(),key=lambda x:x[1],reverse=True)[:k]).keys())
        dic = {}
        freq = [[] for i in range(len(nums)+1)]
     
        for n in nums:
            dic[n] = 1 + dic.get(n,0)
        for a,v in dic.items():
            freq[v].append(a)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res




        