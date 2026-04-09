class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        from collections import defaultdict
        cnt = defaultdict(int)
        for n in nums:
            cnt[n]+=1
        return list(dict(sorted(cnt.items(),key=lambda x:x[1],reverse=True)[:k]).keys())

        