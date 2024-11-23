# 1 Given an array of integers nums and an integer target, return the indices of the two numbers
# such that they add up to target.

def two_sum(nums, target):
    # Dictionary to store the index of numbers
    num_to_index = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]

        # Store the current number with its index
        num_to_index[num] = i

    # If no solution is found
    return None

c=two_sum([3,4,5,3,0,0,3,12,9,3 ],9)
print(c)

# 2.Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three, output "Fizz" instead of the number. For multiples of five, output
# "Buzz". For numbers that are multiples of both three and five, output "FizzBuzz" in python

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Example usage:
n = 15
print("\n".join(fizz_buzz(n)))

# Longest Substring Without Repeating Characters
# Find the length of the longest substring without repeating characters in a string. python

def longestUniqueSubstr(s):

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    maxLength = 0
    visited = [False] * 256
    left = 0
    right = 0
    while right < len(s):
        while visited[ord(s[right])] == True:
            visited[ord(s[left])] = False
            left += 1

        visited[ord(s[right])] = True
        maxLength = max(maxLength, right - left + 1)
        right += 1

    return maxLength

# Example usage:
input_string = "abcefghi"
print(longestUniqueSubstr(input_string))  # Output: 5

# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all elements of nums except nums[i].

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# Example usage:
nums = [1, 2, 3, 4, 3]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]

# You are given an m x n grid where each cell can have one of three values:
# • 0 representing an empty cell.
# • 1 representing a fresh orange.
# • 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes
# rotten. Return the minimum time required to rot all oranges. If it is impossible, return -1.

from collections import deque

def orangesRotting(grid):

    m, n = len(grid), len(grid[0])


    queue = deque()
    fresh_oranges = 0
    time = 0


    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1


    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    while queue and fresh_oranges > 0:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()


            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:

                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx, ny))


        time += 1

    if fresh_oranges > 0:
        return -1

    return time

# Example usage:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 2]
]
print(orangesRotting(grid))  # Output: 4


# Given n non-negative integers representing the elevation map, calculate how much water it can trap after
# raining.

def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

# Example usage:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6

# Given two strings s and t, return the minimum window in s which contains all characters of t.
from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    # Frequency map of characters in t
    t_count = Counter(t)
    required = len(t_count)

    # Sliding window variables
    left, right = 0, 0
    formed = 0
    window_count = Counter()
    min_len = float("inf")
    min_window = ""

    # Start sliding window
    while right < len(s):
        # Add character from the right end of the window
        char = s[right]
        window_count[char] += 1

        # If the current character's count matches the count in t, increment formed
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        # Try to shrink the window from the left
        while left <= right and formed == required:
            char = s[left]

            # Update the minimum window if the current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right+1]

            # Shrink the window from the left
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1

            left += 1

        # Expand the window to the right
        right += 1

    return min_window

# You are given n jobs. Each job has a startTime, endTime, and a profit.
# You need to schedule the jobs such that you maximize your total profit, ensuring that no two jobs
# overlap.
# Return the maximum profit you can achieve.
# Hint:
# • Sort the jobs by their end time.
# • Use binary search to find the latest non-overlapping job for efficient lookups.
#     • Use dynamic programming to store the maximum profit at each step

class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def maxProfit(jobs):

    jobs.sort(key=lambda x: x.end)
    n = len(jobs)
    dp = [0] * (n + 1)

    def find_last_non_overlapping(i):
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid].end <= jobs[i].start:
                if jobs[mid + 1].end <= jobs[i].start:
                    left = mid + 1
                else:
                    return mid
            else:
                right = mid - 1
        return -1

    for i in range(1, n + 1):

        curr_job = jobs[i - 1]

        include_profit = curr_job.profit
        last_non_overlapping_index = find_last_non_overlapping(i - 1)
        if last_non_overlapping_index != -1:
            include_profit += dp[last_non_overlapping_index + 1]

        dp[i] = max(dp[i - 1], include_profit)

    return dp[n]

# Example usage:
jobs = [Job(1, 3, 50), Job(2, 5, 10), Job(4, 6, 70), Job(6, 7, 20), Job(5, 8, 60)]
print(maxProfit(jobs))  # Output: 140 (Jobs 1 and 4 for max profit)


# Given two sorted arrays nums1 and nums2 of size m and n, return the median of the two sorted
# arrays. The overall run time complexity should be O(log⁡(min⁡(m,n))).

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted properly")

# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5
