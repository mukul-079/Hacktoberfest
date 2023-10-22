# Maximum Score of a Good Subarray

'''
Description: 
You are given an array of integers nums (0-indexed) and an integer k. The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j. Return the maximum possible score of a good subarray.

Python Code Solution : by using Two Pointer
'''

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        n=len(a)-1
        i=k
        j=k
        mini = a[k]
        ans = a[k]
        while(j<n or i>0):
            if(i==0 or (j<n and a[j+1]> a[i-1])):
                j+=1                        
            else:
                i-=1
            mini = min(a[i], a[j], mini)
            ans = max(ans, mini*(j-i+1)) 
        return ans
        


 
