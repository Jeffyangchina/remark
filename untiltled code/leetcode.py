
class Solution:
    def isMatch(self, s):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lon=len(s)
        val=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        for i in range(lon-1,-1,-1):
            num=dic[s[i]]
            if num>=val:
                val+=num
            else:
                val-=num
        return val

s='XI'
p='.*'
h=Solution()

print(h.isMatch(s))
