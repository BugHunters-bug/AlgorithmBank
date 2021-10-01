from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        ret=[]
        q=deque()
        q.append(0)
        visited=[False]*V
        visited[0]=True
        while q:
            size=len(q)
            for i in range(size):
                curr=q.popleft()
                ret.append(curr)
                temp=adj[curr]
                for x in temp:
                    if visited[x]==False:
                        visited[x]=True
                        q.append(x)
        
        return ret
        # code here

#{ 
#  Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

# } Driver Code Ends