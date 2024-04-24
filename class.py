class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if i >= k:
                window.remove(nums[i - k])
        return False
solution = Solution()
a = [1,2,3,1,2,3]
b=2
print(solution.containsNearbyDuplicate(a,b))
