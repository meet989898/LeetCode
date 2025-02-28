class LinkedList:
    def __init__(self, s: str):
        self.parent = None
        self.len = len(s)
        self.s = s

    def __len__(self) -> int:
        return self.len
    
    def append(self, s: str) -> "LinkedList":
        parent = self
        nxt = LinkedList(s)
        nxt.parent = parent
        nxt.len += parent.len
        return nxt
    
    def to_str(self) -> str:
        q = deque()
        cur = self
        while cur:
            q.appendleft(cur.s)
            cur = cur.parent
        return "".join(q)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:        
        if len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            longer, shorter = str2, str1
        
        R = len(longer)
        C = len(shorter)
        prev_dp = [LinkedList(shorter[:c]) for c in range(C + 1)]

        for r in range(1, R + 1):
            dp = [None] * (C + 1)
            dp[0] = LinkedList(longer[:r])
            
            for c in range(1, C + 1):
                lch, sch = longer[r - 1], shorter[c - 1]
                
                if lch == sch:
                    dp[c] = prev_dp[c - 1].append(lch)
                else:
                    use_short = dp[c - 1].append(sch)
                    use_long = prev_dp[c].append(lch)
                    dp[c] = use_short if len(use_short) < len(use_long) else use_long
            
            prev_dp = dp

        return dp[C].to_str()