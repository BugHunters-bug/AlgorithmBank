
class Solution:
    def findTwoElement( self,arr, n):
        memo={}
        missing=0
        for i in arr:
            if i in memo:
                repeating=i
            else:
                memo[i]=1
        for i in range(1,n+1):
            if i not in memo:
                missing =i
                
        return repeating,missing
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends