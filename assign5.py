#1. Second-largest unique element (without sort() or max())
'''
def second_largest(arr):
    largest = second = None

    for num in arr:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

print(second_largest([10, 20, 4, 20, 15]))
'''

#2. Find all pairs whose sum equals target
'''
def find_pairs(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))

        seen.add(num)

    return list(pairs)

print(find_pairs([2, 4, 3, 5, 7, 1], 6))
'''

#3. Move all zeros to the end of an array without changing the order of other elements.
'''
def move_zeros(arr):
    result = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(result))
    return result + zeros

print(move_zeros([0, 1, 0, 3, 12]))
'''

#4. Find the missing number from an array containing numbers from 1 to N.
'''
def missing_number(arr, n):
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual

print(missing_number([1, 2, 4, 5], 5))
'''

#5. Find all duplicate elements in a list without using nested loops.
'''
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))
'''

#6. Find the first non-repeating character in a string.
'''
def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char

    return None

print(first_non_repeating("aabbcde"))
'''

#7. Check whether two strings are anagrams without using sorted().
'''
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True

print(are_anagrams("listen", "silent"))
'''

#8. Merge two sorted arrays without using sort().
'''
def merge_arrays(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

print(merge_arrays([1, 3, 5], [2, 4, 6]))
'''

#9. Rotate an array to the right by K positions.
'''
def rotate_right(arr, k):
    if not arr:
        return arr

    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr

print(rotate_right([1, 2, 3, 4, 5], 2))
'''

#10. Find the intersection of two arrays, including duplicate occurrences.
'''
from collections import Counter

def intersection(a, b):
    count = Counter(a)
    result = []

    for num in b:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result

print(intersection([1, 2, 2, 3], [2, 2, 2, 3]))
'''

#11. Find the maximum sum of a contiguous subarray.
'''
def max_subarray_sum(arr):
    current = best = arr[0]

    for num in arr[1:]:
        current = max(num, current + num)
        best = max(best, current)

    return best

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
'''

#12. Find the longest substring without repeating characters.
'''
def longest_substring(s):
    seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        longest = max(longest, right - left + 1)

    return longest

print(longest_substring("abcabcbb"))
'''

#13. Find the longest common prefix among multiple strings.
'''
def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))
'''

#14. Group a list of strings into anagram groups.
'''
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
'''

#15. Find the Kth largest element in an unsorted array.
'''
def kth_largest(arr, k):
    unique = list(set(arr))

    if k < 1 or k > len(unique):
        return None

    def quickselect(nums, target):
        pivot = nums[len(nums) // 2]

        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        smaller = [x for x in nums if x < pivot]

        if target <= len(greater):
            return quickselect(greater, target)

        elif target <= len(greater) + len(equal):
            return pivot

        else:
            return quickselect(
                smaller,
                target - len(greater) - len(equal)
            )

    return quickselect(unique, k)

print(kth_largest([3, 2, 1, 5, 6, 4], 2))
'''

#16. Check whether a given string contains balanced parentheses using a stack.
'''
def balanced_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

print(balanced_parentheses("{[()]}"))

print(balanced_parentheses("{[(])}"))
'''

#17. Find all subarrays whose sum equals a given target.
'''
def subarrays_with_sum(arr, target):
    result = []

    for start in range(len(arr)):
        total = 0

        for end in range(start, len(arr)):
            total += arr[end]

            if total == target:
                result.append(arr[start:end + 1])

    return result

print(subarrays_with_sum([1, 2, 3, 2], 5))
'''

#18. Merge overlapping intervals in a list.
'''
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]))
'''

#19. Search for an element in a rotated sorted array.
'''
def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
'''

#20. Find the longest consecutive sequence in an unsorted array.
'''
def longest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            length = 1
            current = num

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
'''

#21. Find the trapped rainwater between elevation bars.
'''
def trapped_water(height):
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water

print(trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
'''

#22. Find the median of two sorted arrays in O(log(m+n)) time.
'''
def median_two_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        a_left = float("-inf") if i == 0 else a[i - 1]
        a_right = float("inf") if i == m else a[i]

        b_left = float("-inf") if j == 0 else b[j - 1]
        b_right = float("inf") if j == n else b[j]

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return max(a_left, b_left)

            return (max(a_left, b_left) +
                    min(a_right, b_right)) / 2

        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1

    return None

print(median_two_arrays([1, 3], [2]))
print(median_two_arrays([1, 2], [3, 4]))
'''

#23. Find the maximum product of a contiguous subarray.
'''
def max_product_subarray(arr):
    maximum = minimum = result = arr[0]

    for num in arr[1:]:
        if num < 0:
            maximum, minimum = minimum, maximum

        maximum = max(num, maximum * num)
        minimum = min(num, minimum * num)

        result = max(result, maximum)

    return result

print(max_product_subarray([2, 3, -2, 4]))
'''

#24. Find the smallest missing positive integer from an unsorted array.
'''
def smallest_missing_positive(arr):
    nums = set(arr)
    number = 1

    while number in nums:
        number += 1

    return number

print(smallest_missing_positive([3, 4, -1, 1]))
'''

#25. Count the number of subarrays whose sum equals K.
'''
def count_subarrays(arr, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix_sum += num

        count += freq.get(prefix_sum - k, 0)

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

print(count_subarrays([1, 1, 1], 2))
'''

#26. Find the longest increasing subsequence in an array.
'''
def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
'''

#27. Solve the Coin Change problem using dynamic programming.
'''
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(
                dp[value],
                dp[value - coin] + 1
            )

    return dp[amount] if dp[amount] != float("inf") else -1

print(coin_change([1, 2, 5], 11))
'''

#28. Solve the Word Break problem using dynamic programming.
'''
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[len(s)]

print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
'''

#29. Find the minimum number of jumps required to reach the last index.
'''
def min_jumps(arr):
    n = len(arr)

    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= n - 1:
                return jumps

            if current_end == i:
                return -1

    return -1

print(min_jumps([2, 3, 1, 1, 4]))
'''

#30. Find the maximum profit from buying and selling stocks with multiple transactions.
'''
def max_stock_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

print(max_stock_profit([7, 1, 5, 3, 6, 4]))
'''

#31. Implement an LRU Cache with O(1) time complexity for get() and put().
'''
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  

cache.put(3, 30)

print(cache.get(2))  
print(cache.get(3))  
'''

#32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

s = MinStack()
s.push(5)
s.push(3)
s.push(7)

print(s.getMin())  
print(s.top())     
s.pop()
print(s.getMin())  
'''

#33. Find the number of islands in a 2D matrix using DFS or BFS.
'''
def number_of_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] != "1"):
            return

        grid[r][c] = "0"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count


grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"]
]

print(number_of_islands(grid))
'''

#34. Find the shortest path in a weighted graph using Dijkstra's algorithm.
'''
import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        distance, node = heapq.heappop(heap)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8)],
    "D": [("B", 5), ("C", 8)]
}

print(dijkstra(graph, "A"))
'''

#35. Detect a cycle in a directed and undirected graph.
'''
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True

            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


graph_undirected = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

print(has_cycle_undirected(graph_undirected))
'''

#36. Implement topological sorting for a directed acyclic graph.
'''
from collections import deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return []  # Cycle exists

    return result


graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

print(topological_sort(graph))
'''

#37. Solve the N-Queens problem using backtracking.
'''
def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            safe = True

            for previous_row in range(row):
                previous_col = board[previous_row].index("Q")

                if previous_col == col:
                    safe = False
                    break

                if abs(previous_col - col) == abs(previous_row - row):
                    safe = False
                    break

            if safe:
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return solutions


solutions = solve_n_queens(4)

for solution in solutions:
    for row in solution:
        print(row)
    print()
'''

#38. Generate all permutations of a given string or array without duplicates.
'''
def unique_permutations(arr):
    arr.sort()
    result = []
    used = [False] * len(arr)

    def backtrack(path):
        if len(path) == len(arr):
            result.append(path.copy())
            return

        for i in range(len(arr)):
            if used[i]:
                continue

            if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(arr[i])

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


print(unique_permutations([1, 1, 2]))

#39. Serialize and deserialize a binary tree.

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def serialize(root):
    if not root:
        return "[]"

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("None")

    while result[-1] == "None":
        result.pop()

    return ",".join(result)


def deserialize(data):
    if data == "[]":
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] != "None":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "None":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = serialize(root)
print(data)

new_root = deserialize(data)
print(new_root.val)
'''

#40. Find the lowest common ancestor of two nodes in a binary tree.

def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left       
q = root.right     

result = lowest_common_ancestor(root, p, q)
print(result.val)
