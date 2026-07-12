class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #if sorted - use binary search
        
        #left=0
        #right=len(numbers)-1
        #while left<right:
        #    cursum=numbers[left]+numbers[right]
        #    if cursum==target:
        #        return [left+1,right+1]
        #    elif cursum>target:
        #        right-=1
        #    else:
        #        left+=1
        #return []

        for i in range(len(numbers)):
            l,r=i+1,len(numbers)-1
            temp=target-numbers[i]
            while l<=r:
                mid=l+(r-l)//2
                if numbers[mid]==temp:
                    return [i+1,mid+1]
                elif numbers[mid]<temp:
                    l=mid+1
                else:
                    r=mid-1
        return []
            


        