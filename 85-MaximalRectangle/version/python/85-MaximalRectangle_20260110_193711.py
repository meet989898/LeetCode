# Last updated: 1/10/2026, 7:37:11 PM
1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        r, c=len(matrix), len(matrix[0])
4        if r==1 and c==1:
5            if matrix[0][0]=='1': return 1
6            else: return 0
7        h=[0]*(c+1)
8        maxArea=0
9
10        for i, row  in enumerate(matrix):
11            st=[-1] 
12            row.append('0')
13            for j, x in enumerate(row):
14                # build h
15                if x=='1': h[j]+=1
16                else: h[j]=0
17                # mononotonic stack has at leat element -1
18                while len(st)>1 and (j==c or h[j]<h[st[-1]]):
19                    m=st[-1]
20                    st.pop()
21                    w=j-st[-1]-1
22                    area=h[m]*w
23                    maxArea=max(maxArea, area)
24                st.append(j)
25        return maxArea