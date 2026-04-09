class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        
        # for s in strs:
        #     sorted_word = tuple(sorted(s))
        #     res[sorted_word].append(s)
            
        # return list(res.values())
        di = defaultdict(list)
        for s in strs:
            ch = [0]*26
            for c in s:
                ch[ord(c) - ord('a')] += 1
       
            di[tuple(ch)].append(s)
        return list(di.values())
        


        