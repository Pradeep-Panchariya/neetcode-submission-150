class Solution:

    def encode(self, strs: List[str]) -> str:
       string = ''
       for i in strs:
          string += str(len(i)) + '#' + i
       print(string)
       return string



    def decode(self, s: str) -> List[str]:
        lst=[]
        i=0
        while i < len(s):
            j = i 
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            ans = s[j+1:j+length+1]
            lst.append(ans)
            i= j+length+1

        return lst




