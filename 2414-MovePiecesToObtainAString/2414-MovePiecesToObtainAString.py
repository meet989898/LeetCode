# Last updated: 10/7/2025, 10:28:40 AM
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        s = start
        t = target
        n=len(s)
        
        s+='@'
        t+='@'

        i, j=0, 0
        while i<n or j<n:
            while i<n and s[i]=='_': i+=1
            while j<n and t[j]=='_': j+=1
            c=s[i]
            if c!=t[j]: return False
            if c=='L' and i<j: return False
            if c=='R' and i>j: return False
            i+=1
            j+=1
        return True