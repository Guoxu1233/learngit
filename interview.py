import math


class Solution:
    def findMaxAverage(self, nums, k):
        # Step 1
        # 定义需要维护的变量
        # 本题求最大平均值 (其实就是求最大和)，所以需要定义sum_, 同时定义一个max_avg (初始值为负无穷)
        sum_ = 0
        max_avg = -math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (sum_, max_avg), 不断把当前值积累到sum_上
            sum_ += nums[end]
            if end - start + 1 == k:
                max_avg = max(max_avg, sum_ / k)

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_)
            if end >= k - 1:
                sum_ -= nums[start]
                start += 1
        # Step 5: 返回答案
        return max_avg


# solution = Solution()
# a = solution.findMaxAverage([1,12,-5,-6,50,3],4)
# print(a)


# def rotate(nums,k):
#     n = len(nums)
#     k = k%n
#     tmp = nums[n-k:].copy()
#     for i in range(n-k-1,-1,-1):
#         nums[i+k] = nums[i]
#     for j in range(0,k):
#         nums[j] = tmp[j]
#
# num = [1,2,3,4,5,6,7]
# a = 3
# rotate(num,a)
# print(num)

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Step 1: 定义需要维护的变量, 本题求最大长度，所以需要定义max_len, 该题又涉及去重，因此还需要一个哈希表
        max_len, hashmap = 0, {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3
            # 更新需要维护的变量 (max_len, hashmap)
            # i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1#get 方法用于从 hashmap 中获取 s[end] 这个键对应的值,如果没有就返回0
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end - start + 1)

            # Step 4:
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        # Step 5: 返回答案 (最大长度)
        return max_len

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))